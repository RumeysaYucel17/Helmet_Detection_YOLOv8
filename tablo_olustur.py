import matplotlib.pyplot as plt

# Veriler
columns = ["Deney", "Model", "Veri", "imgsz", "Epoch", "mAP50", "mAP50-95", "Not"]
data = [
    ["v1", "yolov8n", "220 gör.", "640", "100", "0.612", "0.381", "Taban model"],
    ["v2", "yolov8n", "480 gör.", "640", "100", "0.744", "0.489", "Veri iki katina cikti"],
    ["v3", "yolov8s", "480 gör.", "640", "150", "0.801", "0.542", "Model büyütüldü"],
    ["v4", "yolov8s", "480 gör.", "960", "150", "0.836", "0.571", "Küçük nesneler düzeldi"]
]

fig, ax = plt.subplots(figsize=(10, 3))
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.8)

plt.savefig("deney_tablosu.png", bbox_inches='tight', dpi=300)
print("Tablo 'deney_tablosu.png' olarak kaydedildi!")