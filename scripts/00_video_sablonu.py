import cv2
import time

# 0 -> varsayılan webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Kamera veya video kaynağı açılamadı!")

fps_kaynak = cap.get(cv2.CAP_PROP_FPS)
genislik = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
yukseklik = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Kaynak: {genislik}x{yukseklik} @ {fps_kaynak:.1f} fps")

# Çıktı kaydetmek için VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("outputs/cikti.mp4", fourcc, 25, (genislik, yukseklik))

prev = time.time()

while True:
    ok, frame = cap.read()
    if not ok:
        break

    # ---- BURADA MODEL ÇALIŞACAK ----

    # FPS hesabı
    simdi = time.time()
    fps = 1 / (simdi - prev) if (simdi - prev) > 0 else 0
    prev = simdi

    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Kaydet ve Göster
    out.write(frame)
    cv2.imshow("Akis", frame)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()