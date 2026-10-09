# Geri Dönüşüm Tespiti
## YOLOv8 ile Nesne Algılama Projesi

Bu proje, **YOLOv8** kullanılarak geri dönüştürülebilir atıkların (ör. plastik, cam, metal vb.) görüntüler üzerinden **nesne algılama (object detection)** yöntemiyle tespit edilmesini amaçlamaktadır.

Proje; veri seti eğitimi, model oluşturma ve tek bir görüntü üzerinde tahmin adımlarını içermektedir.

---

## 🎯 Projenin Amacı

- Geri dönüştürülebilir atıkları otomatik olarak tespit etmek
- YOLOv8 mimarisi ile nesne algılama pratiği yapmak
- Kendi veri seti ile model eğitme ve test sürecini öğrenmek

---

## 📂 Proje Yapısı

```text
.
├── README.md
├── Geri Donusum Tespiti.v1-dataset.yolov8.zip   # YOLOv8 formatında veri seti
├── train_yolov8m.py                             # YOLOv8m eğitim scripti
└── predict_image.py                             # Tek görüntü üzerinde tahmin
```

---

## 📊 Veri Seti

`Geri Donusum Tespiti.v1-dataset.yolov8.zip` dosyası, YOLOv8 formatında etiketlenmiş görüntüleri içerir. Zip içeriği:

```text
├── data.yaml
├── README.dataset.txt
├── README.roboflow.txt
├── train/
│   ├── images/   # 400 görüntü (.jpg)
│   └── labels/   # 400 etiket dosyası
├── valid/
│   ├── images/   # 50 görüntü
│   └── labels/   # 50 etiket dosyası
└── test/
    ├── images/   # 50 görüntü
    └── labels/   # 50 etiket dosyası
```

⚠️ Veri seti, eğitime başlamadan önce zip dosyasından çıkarılmalıdır.

---

## 🧠 Kullanılan Model

- **YOLOv8m** (`yolov8m.pt`)
- Nesne algılama (Object Detection)
- Önceden eğitilmiş (pretrained) ağırlıklardan başlanarak eğitim yapılır

---

## ⚙️ Eğitim (Training)

`train_yolov8m.py` içindeki ayarlar:

| Parametre | Değer |
|---|---|
| `DATA_YAML` | Zip'ten çıkarılan klasördeki `data.yaml` yolu (script içinde mutlak Windows yolu olarak tanımlı) |
| `MODEL_NAME` | `yolov8m.pt` |
| `EPOCHS` | 150 |
| `IMGSZ` | 640 |
| `BATCH` | 8 |
| `DEVICE` | 0 (GPU) |
| `WORKERS` | 2 |
| `PROJECT_DIR` | `runs_recycling` |
| `RUN_NAME` | `yolov8m_4class_e150` |

Modeli eğitmek için önce `DATA_YAML` yolunu kendi bilgisayarınıza göre güncelleyin, ardından:

```bash
python train_yolov8m.py
```

Eğitim çıktıları `runs_recycling/yolov8m_4class_e150/` klasörüne kaydedilir; en iyi model `runs_recycling/yolov8m_4class_e150/weights/best.pt` yoludur.

---

## 🔍 Tahmin (Inference)

`predict_image.py` içindeki ayarlar:

- `MODEL_PATH`: Eğitim scriptinin ürettiği `runs_recycling/yolov8m_4class_e150/weights/best.pt`
- `CONF = 0.25`, `IMGSZ = 640`, `DEVICE = 0` (GPU)

Görüntü yolu komut satırından verilir:

```bash
python predict_image.py ornek.jpg
```

Script:

- tespit edilen nesneleri confidence değerine göre büyükten küçüğe sıralayarak sınıf adı, confidence ve bounding box koordinatlarıyla konsola yazdırır,
- bounding box'ların çizildiği görüntüyü OpenCV penceresinde gösterir,
- tahmin görselini kaydeder (`save=True`) ve kayıt klasörünü yazdırır.

---

## 📈 Sonuçlar

Depoda eğitim çıktıları (metrikler, `runs_recycling/` klasörü) bulunmadığından sayısal sonuçlar burada verilmemiştir.

---

## 🛠️ Kullanılan Teknolojiler

- Python
- Ultralytics YOLOv8
- OpenCV
- PyTorch (Ultralytics üzerinden)

---

## ▶️ Kurulum

Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

> Not: `DEVICE = 0` ayarı CUDA destekli bir GPU gerektirir. GPU yoksa script içinde `DEVICE = "cpu"` olarak değiştirilebilir.

---

## 📌 Notlar

- Proje eğitim ve geliştirme amaçlıdır
- Gerçek zamanlı sistemler için ek optimizasyonlar gerekebilir
- Model performansı veri setinin kalitesine doğrudan bağlıdır
