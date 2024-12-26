import os
import csv
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Load sensitive info from environment variables
IOT_ENDPOINT = os.getenv("IOT_ENDPOINT")
THING_NAME = os.getenv("THING_NAME")
CERT_PATH = os.getenv("CERT_PATH", "certs/Temperature_Sensor.cert.pem")
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", "certs/Temperature_Sensor.private.key")
ROOT_CA_PATH = os.getenv("ROOT_CA_PATH", "certs/AmazonRootCA1.pem")
CSV_FILE = "data/temperature_data.csv"
TOPIC = "sensor/temperature"

# MQTT Client Setup
mqtt_client = AWSIoTMQTTClient(THING_NAME)
mqtt_client.configureEndpoint(IOT_ENDPOINT, 8883)
mqtt_client.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERT_PATH)

mqtt_client.configureOfflinePublishQueueing(-1)
mqtt_client.configureDrainingFrequency(2)
mqtt_client.configureConnectDisconnectTimeout(60)
mqtt_client.configureMQTTOperationTimeout(30)

mqtt_client.connect()

def publish_temperature_data():
    with open(CSV_FILE, 'r') as file:
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
    publish_temperature_data()
    mqtt_client.disconnect()
