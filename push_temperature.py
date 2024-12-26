import os
import csv
import time
import json
import boto3
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Load sensitive info from environment variables
IOT_ENDPOINT = os.getenv("IOT_ENDPOINT")
THING_NAME = os.getenv("THING_NAME")
CERT_PATH = os.getenv("CERT_PATH", "certs/device.cert.pem")
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", "certs/device.private.key")
ROOT_CA_PATH = os.getenv("ROOT_CA_PATH", "certs/AmazonRootCA1.pem")
TOPIC = "sensor/temperature"

# S3 Configuration
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_OBJECT_KEY = os.getenv("S3_OBJECT_KEY")
LOCAL_CSV_PATH = "data/temperature_data.csv"

# Initialize S3 Client
s3 = boto3.client('s3')

# Download CSV from S3
def download_csv_from_s3():
    try:
        s3.download_file(S3_BUCKET_NAME, S3_OBJECT_KEY, LOCAL_CSV_PATH)
        print(f"Downloaded {S3_OBJECT_KEY} from {S3_BUCKET_NAME} to {LOCAL_CSV_PATH}")
    except Exception as e:
        print(f"Failed to download CSV from S3: {str(e)}")
        exit(1)

# MQTT Client Setup
mqtt_client = AWSIoTMQTTClient(THING_NAME)
mqtt_client.configureEndpoint(IOT_ENDPOINT, 8883)
mqtt_client.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERT_PATH)

mqtt_client.configureOfflinePublishQueueing(-1)
mqtt_client.configureDrainingFrequency(2)
mqtt_client.configureConnectDisconnectTimeout(60)
mqtt_client.configureMQTTOperationTimeout(30)

mqtt_client.connect()

# Publish Temperature Data to AWS IoT
def publish_temperature_data():
    with open(LOCAL_CSV_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            payload = {
                "timestamp": row["Timestamp"],
                "temperature": float(row["Temperature"])
            }
            mqtt_client.publish(TOPIC, json.dumps(payload), 1)
            print(f"Published: {payload}")
            time.sleep(5)

if __name__ == "__main__":
    download_csv_from_s3()
    publish_temperature_data()
    mqtt_client.disconnect()
    print("Disconnected from AWS IoT Core.")
