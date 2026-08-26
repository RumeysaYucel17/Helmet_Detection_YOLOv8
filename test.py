import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO("best.pt")

# Webcam başlat
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # conf=0.70: Baretleri kaçırmayan, aşırı kararsız tahminleri süzceksen optimal eşik
    # iou=0.45: Çakışan kutuları temizler
    results = model(frame, conf=0.70, iou=0.45)

    # Kare üzerine çizdir
    annotated_frame = results[0].plot()

    # Ekranı göster
    cv2.imshow("Kask Tespiti (Optimal Test)", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()