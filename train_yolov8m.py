from ultralytics import YOLO
import os

# ==== AYARLAR ====
DATA_YAML = r"C:\Users\okaan\Downloads\goruntu isleme\Geri Donusum Tespiti.v1-dataset.yolov8\data.yaml"  # data.yaml yolu
MODEL_NAME = "yolov8m.pt"  # ✅ YOLOv8m

EPOCHS = 150
IMGSZ = 640
BATCH = 8            # YOLOv8m için genelde daha güvenli (VRAM iyiyse 16 deneyebilirsin)
DEVICE = 0           # ✅ GPU
WORKERS = 2

PROJECT_DIR = "runs_recycling"
RUN_NAME = "yolov8m_4class_e150"  # klasör adı

def main():
    assert os.path.exists(DATA_YAML), "data.yaml bulunamadı"

    model = YOLO(MODEL_NAME)

    model.train(
        data=DATA_YAML,
        epochs=EPOCHS,
        imgsz=IMGSZ,
        batch=BATCH,
        device=DEVICE,
        workers=WORKERS,
        project=PROJECT_DIR,
        name=RUN_NAME
    )

    best_path = os.path.join(PROJECT_DIR, RUN_NAME, "weights", "best.pt")
    print("\n✅ Eğitim tamamlandı")
    print("📂 En iyi model:", best_path)

if __name__ == "__main__":
    main()
