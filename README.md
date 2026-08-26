# 🪖 Safety Helmet Detection using YOLOv8

Bu proje, iş sağlığı ve güvenliği (İSG) standartlarına uygun olarak şantiye, fabrika ve endüstriyel alanlarda çalışanların **kask (baret) takıp takmadıklarını** gerçek zamanlı olarak tespit etmek amacıyla geliştirilmiş bir Bilgisayarlı Görü (Computer Vision) projesidir.

---

## 📌 Özellikler

- **YOLOv8 Tabanlı Nesne Tespiti:** Yüksek doğruluk (mAP) ve düşük çıkarım süresi.
- **Model Karşılaştırmalı Deneyler:** Farklı hiperparametre ve model boyutları (`yolov8n`, `yolov8m` vb.) ile gerçekleştirilmiş performans analizleri.
- **Esnek Test Seçenekleri:** Görsel ve video girdileri üzerinde anlık çıkarım yapabilme.
- **Otomatik Raporlama:** Deney metriklerini tabloya dönüştüren yardımcı araçlar (`tablo_olustur.py`).

---

## 📊 Deney Sonuçları & Metrikler

Farklı konfigürasyonlarla yapılan eğitimlerin başarım karşılaştırması aşağıda verilmiştir:

![Deney Tablosu](deney_tablosu.png)
---
## 📁 Veri Seti (Dataset)

Projede kullanılan kask tespiti veri setine Roboflow Universe üzerinden erişebilirsiniz:
- 🔗 **Dataset Linki:** [Roboflow - Helmet Detection Dataset](https://universe.roboflow.com/helmet-detection-sutvo/helmet-detection-j7vt9)
---

## 🛠️ Kurulum

1. Repoyu bilgisayarınıza klonlayın:
```bash
git clone [https://github.com/RumeysaYucel17/Helmet_Detection_YOLOv8.git](https://github.com/RumeysaYucel17/Helmet_Detection_YOLOv8.git)
cd Helmet_Detection_YOLOv8