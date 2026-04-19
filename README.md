AWS IoT & MQTT Real-Time System Monitor 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05032.svg?style=for-the-badge&logo=git&logoColor=white)

Bu proje, yerel bir cihazın sistem kaynaklarını (CPU/RAM) gerçek zamanlı olarak izleyen ve MQTT protokolü üzerinden AWS Bulut ekosistemine aktaran bir uçtan uca IoT çözümüdür.

---

Projenin Amacı
Ankara Üniversitesi Bilgisayar Mühendisliği, Bulut Bilişim dersi kapsamında geliştirilen bu çalışma; verilerin sensörlerden (bu projede sistem kaynakları) buluta güvenli iletimini, bulut üzerinde işlenmesini ve NoSQL veritabanında depolanmasını uygulamalı olarak göstermektedir.

Sistem Mimarisi
Proje akışı şu şekildedir:
1. Veri Toplama: psutil ile yerel cihazdan telemetri verilerinin okunması.
2. Güvenli Bağlantı: X.509 sertifikaları ile TLS/SSL üzerinden AWS IoT Core bağlantısı.
3. Mesajlaşma: MQTT protokolü ile sdk/test/python konusuna (topic) yayın yapılması.
4. Kural Motoru (Rule Engine): Gelen verilerin AWS IoT üzerinden SQL sorgusuyla yakalanması.
5. Depolama: Yakalanan verilerin anlık olarak **Amazon DynamoDB** (SystemMetrics tablosu) içine yazılması.

Teknik Stack
Katman                    Teknoloji 
Programlama               Python 3.x 
Mesajlaşma Protokolü      MQTT (Message Queuing Telemetry Transport) 
Bulut Sağlayıcı           Amazon Web Services (AWS) 
IoT Servisi               AWS IoT Core 
Veritabanı                Amazon DynamoDB (NoSQL) 
Güvenlik                  AWS IoT Policies & X.509 Certificates 

Kurulum ve Kullanım

1. Hazırlık
Önce projenin bağımlılıklarını kurun:

pip install AWSIoTPythonSDK psutil

2. Sertifikalar

certs/ klasörü altına AWS'den aldığınız sertifikaları ekleyin. (Güvenlik nedeniyle bu dosyalar GitHub'a yüklenmemiştir).

3. Çalıştırma

python main.py
Veri Örneği (Payload)
AWS'ye iletilen mesajın yapısı:

{
  "device_id": "Laptop_Sensor",
  "timestamp": 1712345678,
  "cpu_usage": 12.5,
  "ram_usage": 74.2
}
Hazırlayan: Ayşe Ceren Şenel
