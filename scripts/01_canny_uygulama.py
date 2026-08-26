import cv2

# Kamerayı aç
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Kamera açılamadı!")

print("Uygulama başladı! 's' tuşu ile snapshot alın, 'q' tuşu ile çıkın.")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    # 1. Kareyi gri tonlamaya çevir
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Parazitleri temizlemek için hafif bulanıklaştır ve Canny kenarlarını bul
    blur = cv2.GaussianBlur(gri, (5, 5), 0)
    kenar = cv2.Canny(blur, 100, 200)

    # 3. Kenar görüntüsünü ekranda göster
    cv2.imshow("Canny Kenar Tespiti", kenar)

    # Klavyeden basılan tuşu dinle
    key = cv2.waitKey(1) & 0xFF

    # 's' tuşuna basılırsa anlık kareyi snapshot.jpg olarak kaydet
    if key == ord('s'):
        cv2.imwrite("outputs/snapshot.jpg", kenar)
        print("Snapshot başarıyla 'outputs/snapshot.jpg' konumuna kaydedildi!")

    # 'q' tuşuna basılırsa çık
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()