from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    results = model.train(
        data="datasets/kask_tespit/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        device=0,  # GPU gücünü kullanıyoruz
        project="runs/detect",
        name="kask_v1"
    )

if __name__ == '__main__':
    main()