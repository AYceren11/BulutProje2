import time
import json
import psutil # Sistem verilerini (CPU/RAM) okumak için
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


ENDPOINT = "a37b0n2j0e4tm9-ats.iot.eu-north-1.amazonaws.com" 
CLIENT_ID = "Laptop_Sensor"

print("1. Dosya yolları kontrol ediliyor...")
# Bu isimlerin klasördekiyle birebir aynı olduğundan emin ol (uzantılar dahil!)
# Terminal çıktısındaki gerçek isimleri buraya yazdık
PATH_TO_CERT = "certs/cert.crt.crt"
PATH_TO_KEY = "certs/private.key.key"
PATH_TO_ROOT = "certs/root.pem"
print("2. Bağlantı yapılandırılıyor...")
myClient = AWSIoTMQTTClient(CLIENT_ID)
myClient.configureEndpoint(ENDPOINT, 8883)
myClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

print("3. AWS IoT Core'a bağlanmaya çalışılıyor (Burada bekliyorsa sertifika veya internet hatasıdır)...")
myClient.connect()
print("4. Bağlantı BAŞARILI!")
# --- MQTT BAĞLANTISI ---
myClient = AWSIoTMQTTClient(CLIENT_ID)
myClient.configureEndpoint(ENDPOINT, 8883)
myClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

print("Buluta bağlanılıyor...")
myClient.connect()
print("Bağlantı başarılı! Gerçek zamanlı veri akışı başladı...")

try:
    while True:
       
        payload = {
            "device_id": CLIENT_ID,
            "timestamp": int(time.time()),
            "cpu_usage": psutil.cpu_percent(),
            "ram_usage": psutil.virtual_memory().percent
        }
        
       
        myClient.publish("sdk/test/python", json.dumps(payload), 1)
        print(f"Gönderilen Veri: {payload}")
        
        time.sleep(5)
except KeyboardInterrupt:
    myClient.disconnect()
    print("Bağlantı kesildi.")