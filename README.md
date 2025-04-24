
# 🚗 Smart Garage IoT Simulation – Cisco Packet Tracer

Proyek ini adalah simulasi sistem IoT otomatisasi garasi menggunakan Cisco Packet Tracer. Sistem bekerja secara otomatis menggunakan motion detector, lampu, pintu garasi, dan AC yang dikendalikan oleh SBC (Single Board Computer).

Ketika gerakan terdeteksi oleh sensor, sistem akan:

- Menyalakan lampu dengan terang penuh
- Membuka pintu garasi
- Menghidupkan AC

Jika tidak ada gerakan, sistem akan mematikan semua perangkat untuk efisiensi energi.


## ⚙️ Perangkat yang Digunakan

- Motion Sensor (di pin 0)
- Lampu (di pin 1)
- Pintu Garasi (di pin 2)
- Air Conditioner (di pin 3)
- SBC Board


## 🧠 Logika Sistem

```
from gpio import *
from time import *

def main():
	pinMode(0, IN)   # Sensor Gerak
	pinMode(1, OUT)  # Lampu
	pinMode(2, OUT)  # Pintu Garasi
	pinMode(3, OUT)  # AC

	while True:
		value = digitalRead(0)
		if value == 1023:
			customWrite(1, 2)  # Lampu: ON (terang penuh)
			customWrite(2, 1)  # Pintu Garasi: Buka
			customWrite(3, 1)  # AC: ON
		else:
			customWrite(1, 0)  # Lampu: OFF
			customWrite(2, 0)  # Pintu Garasi: Tutup
			customWrite(3, 0)  # AC: OFF
		delay(100)

if __name__ == "__main__":
	main()
```

## 🎯 Tujuan

- Meningkatkan pemahaman tentang sistem kontrol otomatis berbasis sensor.
- Melatih penggunaan SBC dan pemrograman Python di lingkungan simulasi Cisco Packet Tracer.
- Menerapkan arsitektur dasar sistem IoT di bidang otomasi rumah.

