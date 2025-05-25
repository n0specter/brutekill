# 🔓 brutekill

**brutekill** adalah tool brute force sederhana berbasis Python, dibuat untuk melakukan serangan login ke form berbasis HTTP/HTTPS dengan delay smart timer dan deteksi respon server.

Tool ini cocok untuk testing form login yang tidak pakai CAPTCHA dan masih vulnerable terhadap brute force attack.

> ⚠️ Tool ini dibuat untuk **tujuan edukasi dan pengujian sistem milik sendiri atau yang sudah mendapat izin**. Dilarang digunakan untuk aktivitas ilegal.

---

## 🚀 Fitur
- Support protokol HTTP & HTTPS
- Bisa mendeteksi respon gagal atau berhasil dari string dalam response
- Smart delay antar request (biar gak kebanned server)
- Simple dan mudah dipakai siapa pun

---

## ⚙️ Persiapan

### 🔸 Requirements
- Python 3
- `requests` library

Install dulu kalau belum:
```bash
pip install requests
