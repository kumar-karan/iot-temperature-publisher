# IoT Temperature Publisher 🌡️

This project sends temperature data from a CSV file to **AWS IoT Core** using Python and MQTT.  
It uses the **AWSIoTPythonSDK** to securely publish sensor data to AWS IoT for further processing, visualization, or storage.

---

## 🚀 Project Overview

- **Read CSV Temperature Data** 📄
- **Securely Connect to AWS IoT Core** 🔒
- **Publish Data to MQTT Topic** 🔄
- **Real-time Monitoring via AWS IoT Core** 📊

---

## 📂 Project Structure

```
/iot-temperature-publisher
│
├── certs/                         # SSL certificates (excluded from GitHub)
│   ├── device.cert.pem
│   ├── device.private.key
│   └── AmazonRootCA1.pem
│
├── data/                          # CSV files for sensor data
│   └── temperature_data.csv
│
├── scripts/                       # Utility scripts
│   └── gen_csv.py                 # Generates CSV data for testing
│
├── push_temperature.py            # Main Python script to publish data
├── .gitignore                     # Git ignore file
├── .env                           # Environment variables (excluded from GitHub)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## ⚙️ Prerequisites

- **AWS IoT Core** set up with a registered device (Thing).
- Certificates (`.pem`) from AWS IoT Core.
- **Python 3.7+** installed.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/username/iot-temperature-publisher.git
cd iot-temperature-publisher
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Certificates (AWS IoT)

Place the following files in the `certs/` directory:

- **Device Certificate** (`device.cert.pem`)
- **Private Key** (`device.private.key`)
- **Amazon Root CA** (`AmazonRootCA1.pem`)

---

### 4. Create `.env` File (Sensitive Info)

```ini
IOT_ENDPOINT=<your-iot-endpoint>
THING_NAME=<your-thing-name>
CERT_PATH=certs/device.cert.pem
PRIVATE_KEY_PATH=certs/device.private.key
ROOT_CA_PATH=certs/AmazonRootCA1.pem
```

Ensure `.env` is **not uploaded to GitHub** by including it in `.gitignore`.

---

### 5. Generate Sample CSV (Optional)

```bash
python scripts/gen_csv.py
```

This creates `temperature_data.csv` in the `data/` directory.

---

## ▶️ Running the Script

```bash
python push_temperature.py
```

- Publishes temperature data from CSV every 5 seconds to AWS IoT Core.
- Subscribe to the MQTT topic `sensor/temperature` in AWS IoT Core to see incoming data.

---

## 📡 Testing in AWS IoT Core

1. **Go to AWS IoT Core > Test > MQTT Test Client**.
2. **Subscribe** to the topic:
   ```
   sensor/temperature
   ```
3. Monitor the incoming temperature data live.

---

## 🛡️ Security Best Practices

- **Never commit certificates or private keys to GitHub.**
- Restrict MQTT policy permissions after successful testing.
- Regularly rotate certificates and update device credentials.

---

## 🤝 Contributing

Feel free to fork this project and open pull requests to enhance functionality or fix bugs.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📧 Contact

For questions or support, reach out to:

- **GitHub:** [username](https://github.com/username)
