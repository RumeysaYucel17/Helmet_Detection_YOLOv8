import os
import glob
from ultralytics import YOLO

# Modeli yükle
model = YOLO("yolov8n.pt")

# Test edilecek conf değerleri
conf_degerleri = [0.1, 0.25, 0.5, 0.8]

# test_images klasöründeki tüm jpg ve png resimlerini bul
resim_yollari = glob.glob("test_images/*.[jp][pn]g")

if not resim_yollari:
    print("UYARI: 'test_images' klasöründe resim bulunamadı! Lütfen 5 resim ekleyin.")
else:
    print("\n" + "="*50)
    print("CONF PARAMETRESİ TESPİT SAYISI DENEYİ")
    print("="*50)

    # Tablo Başlığı
    header = f"{'Resim Adı':<20} | " + " | ".join([f"conf={c:<4}" for c in conf_degerleri])
    print(header)
    print("-" * len(header))

    # Her resim için farklı conf değerlerini dene
    for resim_yolu in resim_yollari[:5]:  # İlk 5 resmi alır
        resim_adi = os.path.basename(resim_yolu)
        satir = f"{resim_adi:<20} | "
        
        for conf_val in conf_degerleri:
            # Tahmin yap (terminali log ile doldurmamak için verbose=False)
            results = model(resim_yolu, conf=conf_val, verbose=False)
            
            # Tespit edilen nesne sayısı
            tespit_sayisi = len(results[0].boxes)
            satir += f"{tespit_sayisi:<9} | "
        
        print(satir)
    print("="*50 + "\n")