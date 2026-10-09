from ultralytics import YOLO
import cv2
import os
import argparse

# ==== AYARLAR ====
# train_yolov8m.py'nin ürettiği ağırlık dosyası
MODEL_PATH = os.path.join("runs_recycling", "yolov8m_4class_e150", "weights", "best.pt")

CONF = 0.25
IMGSZ = 640
DEVICE = 0   # ✅ GPU

def main():
    parser = argparse.ArgumentParser(description="YOLOv8m ile görsel üzerinde atık tespiti")
    parser.add_argument("image", help="Tahmin yapılacak görselin yolu")
    args = parser.parse_args()
    image_path = args.image

    assert os.path.exists(MODEL_PATH), "Model bulunamadı"
    assert os.path.exists(image_path), "Görsel bulunamadı"

    model = YOLO(MODEL_PATH)

    results = model.predict(
        source=image_path,
        imgsz=IMGSZ,
        conf=CONF,
        device=DEVICE,
        save=True
    )

    r = results[0]
    names = r.names

    print("\n=== TAHMİNLER ===")
    if r.boxes is None or len(r.boxes) == 0:
        print("Nesne bulunamadı")
    else:
        # confidence'a göre büyükten küçüğe sıralayıp yazdıralım
        boxes = list(r.boxes)
        boxes.sort(key=lambda b: float(b.conf[0]), reverse=True)

        for i, box in enumerate(boxes):
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            # bbox koordinatları (istersen raporda kullanırsın)
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            print(f"{i+1}) {names[cls_id]} | confidence={conf:.3f} | bbox=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f})")

    # Görseli ekranda göster
    img = r.plot()
    cv2.imshow("YOLOv8m Prediction", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("\n📁 Çıktı klasörü:", r.save_dir)

if __name__ == "__main__":
    main()
