import time
import json
import psutil
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# --- YAPILANDIRMA ---
ENDPOINT = "a37b0n2j0e4tm9-ats.iot.eu-north-1.amazonaws.com" 
CLIENT_ID = "Laptop_Sensor"

# Sertifika Dosya Yolları
PATH_TO_CERT = "certs/cert.crt.crt"
PATH_TO_KEY = "certs/private.key.key"
PATH_TO_ROOT = "certs/root.pem"

# --- MQTT MÜŞTERİ KURULUMU ---
myClient = AWSIoTMQTTClient(CLIENT_ID)
myClient.configureEndpoint(ENDPOINT, 8883)
myClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

# Bağlantı Ayarları 
myClient.configureAutoReconnectBackoffTime(1, 32, 20)
myClient.configureConnectDisconnectTimeout(10)
myClient.configureMQTTOperationTimeout(5)

# --- BAĞLANTI VE VERİ AKIŞI ---
print("AWS IoT Core'a bağlanılıyor...")
try:
    myClient.connect()
    print("Bağlantı başarılı! Gerçek zamanlı veri akışı başladı...")

    while True:
        # Telemetri verisini oluştur
        payload = {
            "device_id": CLIENT_ID,
            "timestamp": int(time.time()),
            "cpu_usage": psutil.cpu_percent(),
            "ram_usage": psutil.virtual_memory().percent
        }
        
        # Veriyi yayınla
        myClient.publish("sdk/test/python", json.dumps(payload), 1)
        print(f"Gönderilen Veri: {payload}")
        
        time.sleep(5)  # 5 saniyelik periyotlarla gönderim

except Exception as e:
    print(f"Bağlantı sırasında bir hata oluştu: {e}")

except KeyboardInterrupt:
    myClient.disconnect()
    print("\nBağlantı kullanıcı tarafından kesildi.")
