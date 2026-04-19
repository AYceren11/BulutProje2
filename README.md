Proje 2: AWS IoT Core ve MQTT ile Gerçek Zamanlı Sistem İzleme
Bu proje, Ankara Üniversitesi Bilgisayar Mühendisliği bünyesinde verilen Bulut Bilişim ve Uygulamaları (BLM3522) dersi kapsamında geliştirilmiştir. Uygulama, yerel bir cihazın sistem kaynaklarını (CPU ve RAM) anlık olarak izleyen ve MQTT protokolü üzerinden AWS Bulut ekosistemine güvenli bir şekilde aktaran uçtan uca bir IoT çözümüdür.

👤 Öğrenci Bilgileri
Ad Soyad: Ayşe Ceren Şenel

Öğrenci Numarası: 23290973

Bölüm: Bilgisayar Mühendisliği

Ders: Bulut Bilişim ve Uygulamaları (BLM3522)

🚀 Proje Sunumu
GİTHUB Repo: https://github.com/AYceren11/BulutProje2.git

Proje Tanıtım Videosu: [[Youtube Linki]](https://youtu.be/2GqCtGSI_Xw)

🛠 Kullanılan Teknolojiler
Programlama: Python 3.11+

IoT Protokolü: MQTT (Message Queuing Telemetry Transport)

Bulut Platformu: AWS IoT Core

Veritabanı: Amazon DynamoDB (NoSQL)

Güvenlik: X.509 Sertifikaları & TLS 1.2

Versiyon Kontrol: Git & GitHub

🏗 Sistem Mimarisi
Uygulama, verinin yerel cihazdan buluta yolculuğunu kapsayan dört ana katmandan oluşur:

Veri Toplama: Python psutil kütüphanesi ile cihazdan telemetri verilerinin (CPU/RAM) okunması.

Haberleşme: AWS tarafından sağlanan sertifikalarla şifrelenmiş MQTT bağlantısı üzerinden verilerin iletilmesi.

Kural Motoru (Rule Engine): IoT Core üzerinde çalışan SQL tabanlı bir kural ile gelen verilerin yakalanması.

Kalıcı Depolama: Yakalanan verilerin anlık olarak DynamoDB SystemMetrics tablosuna kaydedilmesi.

🛡 Güvenlik ve İzolasyon
Sertifika Yönetimi: Cihaz doğrulaması için AWS IoT Core tarafından üretilen Private Key ve Device Certificate dosyaları kullanılmıştır.

Gizlilik: Güvenlik protokolleri gereği certs/ klasörü ve sanal ortam dosyaları (venv/) .gitignore dosyası ile GitHub takibinden hariç tutulmuştur.

📂 Proje Yapısı
/certs: AWS IoT bağlantı sertifikaları (Güvenlik nedeniyle gizli).

main.py: Sistem verilerini toplayan ve MQTT üzerinden yayınlayan ana Python betiği.

README.md: Proje dökümantasyonu.

Projenin Raporu -> [Proje 2.pdf](https://github.com/user-attachments/files/26874753/Proje.2.pdf)
