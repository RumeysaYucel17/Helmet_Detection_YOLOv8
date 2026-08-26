from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")

    results = model.train(
        data="datasets/kask_tespit/data.yaml",  # Doğru yol eklendi
        epochs=50,
        imgsz=640,
        batch=-1,
        workers=2,
        plots=True,
        name="gorev_kask_50epoch"
    )