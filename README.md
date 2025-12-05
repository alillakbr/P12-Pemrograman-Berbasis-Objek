# Sistem Validasi Registrasi Mahasiswa (SOLID + Logging)

## Deskripsi Proyek
Proyek ini adalah implementasi sistem registrasi mahasiswa yang dibangun menggunakan prinsip desain **SOLID** (SRP, OCP, dan DIP). 

Pada versi ini (Pertemuan 12), kode telah ditingkatkan kualitas komunikasinya dengan menambahkan:
1. **Logging**: Menggantikan fungsi `print()` biasa dengan modul `logging` Python untuk pencatatan aktivitas sistem yang lebih profesional (mendukung level INFO, WARNING, ERROR).
2. **Docstrings**: Dokumentasi inline pada setiap kelas dan metode menggunakan standar *Google Style* untuk memudahkan kolaborasi dan pemeliharaan kode.

## Struktur File
- **`registrasi_logging.py`**: File kode utama yang berisi:
  - **Model**: `Student`
  - **Interfaces**: `IValidationRule`
  - **Rules**: `SksLimitRule`, `PrerequisiteRule`, `JadwalBentrokRule`
  - **Service**: `RegistrationService`
- **`README.md`**: File dokumentasi proyek (file ini).

## Prasyarat
- Python 3.x terinstal di sistem Anda.

## Cara Menjalankan
1. Buka terminal atau command prompt.
2. Masuk ke direktori folder proyek ini:
   ```bash
   cd PBO_Praktikum/Pertemuan_12
