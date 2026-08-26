import os
from ultralytics import YOLO

# Modelleri indir ve yükle
print("yolov8n.pt indiriliyor...")
model_n = YOLO("yolov8n.pt")

print("yolov8m.pt indiriliyor...")
model_m = YOLO("yolov8m.pt")

# Dosya boyutlarını megabayt (MB) cinsinden hesapla
boyut_n = os.path.getsize("yolov8n.pt") / (1024 * 1024)
boyut_m = os.path.getsize("yolov8m.pt") / (1024 * 1024)

print("\n--- MODEL BOYUTLARI ---")
print(f"yolov8n.pt Dosya Boyutu: {boyut_n:.2f} MB")
print(f"yolov8m.pt Dosya Boyutu: {boyut_m:.2f} MB")