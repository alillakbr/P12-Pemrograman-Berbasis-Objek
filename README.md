# Sistem Validasi Registrasi Mahasiswa (SOLID + Logging)

## Deskripsi Proyek
Proyek ini adalah implementasi sistem registrasi mahasiswa yang dibangun menggunakan prinsip desain **SOLID** (SRP, OCP, dan DIP). 

### 1. Penerapan Logging (Menggantikan Print)
Seluruh fungsi `print()` telah diganti dengan modul `logging` Python untuk memberikan output yang lebih informatif.
* **Format Log:** `%(asctime)s %(levelname)s - %(name)s - %(message)s`
* **Penerapan pada Bagian C (`order_logging.py`):**
    * Mencatat proses pembayaran kartu kredit.
    * Mencatat pengiriman notifikasi email.
* **Penerapan pada Bagian D (`registrasi_logging.py`):**
    * **INFO:** Mencatat alur normal (Contoh: "Validasi SKS: OK").
    * **WARNING:** Mencatat validasi yang gagal (Contoh: "SKS melebihi batas").
    * **ERROR:** Mencatat kegagalan fatal saat registrasi ditolak.

### 2. Google Style Docstrings
Setiap Kelas, Interface, dan Metode pada kedua file telah dilengkapi dokumentasi inline.
* **Deskripsi:** Penjelasan singkat tentang tanggung jawab kelas/fungsi.
* **Args:** Penjelasan tipe data dan kegunaan parameter input.
* **Returns:** Penjelasan nilai yang dikembalikan oleh fungsi.

###
3. Cara Menjalankan
1. Buka terminal atau command prompt.
2. Masuk ke direktori folder proyek ini:
   ```bash
   cd PBO_Praktikum/Pertemuan_12
