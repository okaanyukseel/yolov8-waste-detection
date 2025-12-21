# Geri Dönüşüm Tespiti  
## YOLOv8 ile Nesne Algılama Projesi

Bu proje, **YOLOv8** kullanılarak geri dönüştürülebilir atıkların (ör. plastik, cam, metal vb.) görüntüler üzerinden **nesne algılama (object detection)** yöntemiyle tespit edilmesini amaçlamaktadır.

Proje; veri seti eğitimi, model oluşturma ve tek bir görüntü üzerinde tahmin (inference) adımlarını içermektedir.

---

## 🎯 Projenin Amacı

- Geri dönüştürülebilir atıkları otomatik olarak tespit etmek  
- YOLOv8 mimarisi ile nesne algılama pratiği yapmak  
- Kendi veri seti ile model eğitme ve test sürecini öğrenmek  

---

## 📂 Proje Yapısı

```text
├── README.md
├── Geri Donusum Tespiti.v1-dataset.yolov8.zip
├── train_yolov8m.py
└── predict_image.py
📊 Veri Seti
Geri Donusum Tespiti.v1-dataset.yolov8.zip

YOLOv8 formatında etiketlenmiş görüntüler

Train / Validation klasörleri ve data.yaml dosyasını içerir

⚠️ Veri seti, eğitime başlamadan önce zip dosyasından çıkarılmalıdır.

🧠 Kullanılan Model
YOLOv8m

Nesne algılama (Object Detection)

Önceden eğitilmiş (pretrained) ağırlıklar kullanılmıştır

⚙️ Eğitim (Training)
Modeli eğitmek için:


python train_yolov8m.py

Eğitim sırasında:

Veri seti data.yaml üzerinden okunur

Epoch, batch size ve model parametreleri script içerisinden ayarlanabilir

Eğitim çıktıları runs/ klasörü altına kaydedilir

🔍 Tahmin (Inference)
Eğitilmiş model ile tek bir görüntü üzerinde tahmin yapmak için:


python predict_image.py

Girdi görüntüsü script içinde belirtilir

Çıktı, tespit edilen nesneler ve bounding box’lar ile görselleştirilir

🛠️ Kullanılan Teknolojiler
Python

Ultralytics YOLOv8

OpenCV

PyTorch

▶️ Kurulum
Gerekli kütüphaneleri yükleyin:

pip install ultralytics opencv-python

📌 Notlar
Proje eğitim ve geliştirme amaçlıdır

Gerçek zamanlı sistemler için ek optimizasyonlar gerekebilir

Model performansı veri setinin kalitesine doğrudan bağlıdır

