import sys
import platform

print("=" * 55)
print("ORTAM KONTROLÜ")
print("=" * 55)
print(f"Python      : {sys.version.split()[0]} ({platform.system()})")

try:
    import torch
    print(f"PyTorch     : {torch.__version__}")
    print(f"CUDA var mı : {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU         : {torch.cuda.get_device_name(0)}")
        vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"VRAM        : {vram:.1f} GB")
    else:
        print("GPU         : Bulunamadı -> CPU modunda çalışılacak")
except ImportError:
    print("PyTorch     : KURULU DEĞİL")

try:
    import cv2
    print(f"OpenCV      : {cv2.__version__}")
except ImportError:
    print("OpenCV      : KURULU DEĞİL")

try:
    import ultralytics
    print(f"Ultralytics : {ultralytics.__version__}")
    ultralytics.checks()
except ImportError:
    print("Ultralytics : KURULU DEĞİL")