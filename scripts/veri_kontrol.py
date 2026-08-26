"""veri_kontrol.py - veri setinde tutarlılık ve format denetimi."""
from pathlib import Path
from collections import Counter
import cv2

KOK = Path("datasets/kask_tespit")
SINIFLAR = ["kask", "kasksiz", "yelek"]

for split in ["train", "val", "test"]:
    img_dir = KOK / "images" / split
    lbl_dir = KOK / "labels" / split
    if not img_dir.exists():
        continue

    gorseller = [p for p in img_dir.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
    sayac, hata, bos, kutu_toplam = Counter(), [], 0, 0

    for img_p in gorseller:
        lbl_p = lbl_dir / (img_p.stem + ".txt")

        if cv2.imread(str(img_p)) is None:
            hata.append(f"OKUNAMADI: {img_p.name}")
            continue

        if not lbl_p.exists():
            hata.append(f"ETIKET YOK: {img_p.name}")
            continue

        satirlar = [s for s in lbl_p.read_text().strip().split("\n") if s]
        if not satirlar:
            bos += 1
            continue

        for i, satir in enumerate(satirlar, 1):
            parcalar = satir.split()
            if len(parcalar) != 5:
                hata.append(f"{lbl_p.name}:{i} -> 5 alan bekleniyor")
                continue

            c = int(parcalar[0])
            deg = [float(x) for x in parcalar[1:]]

            if not 0 <= c < len(SINIFLAR):
                hata.append(f"{lbl_p.name}:{i} -> gecersiz sinif {c}")
            if any(v < 0 or v > 1 for v in deg):
                hata.append(f"{lbl_p.name}:{i} -> normalize degil {deg}")
            if deg[2] <= 0 or deg[3] <= 0:
                hata.append(f"{lbl_p.name}:{i} -> sifir boyutlu kutu")

            sayac[SINIFLAR[c] if 0 <= c < len(SINIFLAR) else c] += 1
            kutu_toplam += 1

    print(f"\n--- {split.upper()} ---")
    print(f"Goruntu: {len(gorseller)} | Kutu: {kutu_toplam} | Negatif: {bos}")
    for isim, adet in sayac.most_common():
        oran = 100 * adet / kutu_toplam if kutu_toplam else 0
        print(f"  {isim:12s}: {adet:5d} ({oran:.1f}%)")

    if hata:
        print(f"  !! {len(hata)} HATA:")
        for h in hata[:15]:
            print(f"    - {h}")
    else:
        print("  Hata bulunamadi.")