import random, shutil
from pathlib import Path

KAYNAK_IMG = Path("ham_goruntuler")
KAYNAK_LBL = Path("ham_etiketler")
HEDEF      = Path("datasets/kask_tespit")
ORAN       = {"train": 0.7, "val": 0.2, "test": 0.1}
random.seed(42)

for split in ORAN:
    (HEDEF / "images" / split).mkdir(parents=True, exist_ok=True)
    (HEDEF / "labels" / split).mkdir(parents=True, exist_ok=True)

gorseller = sorted([p for p in KAYNAK_IMG.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}])
random.shuffle(gorseller)

n = len(gorseller)
n_train = int(n * ORAN["train"])
n_val   = int(n * ORAN["val"])

bolumler = {
    "train": gorseller[:n_train],
    "val":   gorseller[n_train:n_train + n_val],
    "test":  gorseller[n_train + n_val:],
}

for split, dosyalar in bolumler.items():
    for img in dosyalar:
        shutil.copy(img, HEDEF / "images" / split / img.name)
        lbl = KAYNAK_LBL / (img.stem + ".txt")
        if lbl.exists():
            shutil.copy(lbl, HEDEF / "labels" / split / lbl.name)
        else:
            (HEDEF / "labels" / split / (img.stem + ".txt")).touch()
    print(f"{split:6s}: {len(dosyalar)} goruntu")