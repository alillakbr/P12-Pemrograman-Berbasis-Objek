# Sistem Validasi Registrasi Mahasiswa (SOLID + Logging)

## Deskripsi Proyek
Repository ini berisi implementasi sistem registrasi mahasiswa dan sistem checkout order yang telah ditingkatkan kualitas komunikasinya.

Fokus utama dari tugas ini bukanlah mengubah logika bisnis (yang sudah menerapkan prinsip SOLID dari pertemuan sebelumnya), melainkan mengubah kode agar siap produksi (Production-Ready). Kode ini dirancang agar mudah dibaca oleh pengembang lain melalui dokumentasi inline dan mudah dilacak aktivitasnya melalui sistem logging yang terstruktur.

## Struktur File

1. **registrasi_logging.py (Tugas Mandiri)**
   Sistem Validasi KRS Mahasiswa. File ini menerapkan logging untuk setiap aturan validasi:
   - Validasi batas SKS.
   - Validasi mata kuliah prasyarat.
   - Validasi jadwal bentrok.

2. **order_logging.py (Latihan Praktikum)**
   Sistem Checkout E-Commerce. File ini menerapkan logging untuk proses pembayaran kartu kredit dan pengiriman notifikasi email.

3. **README.md**
   Menjelaskan isi dari Proyek.

---

## Fitur dan Implementasi Teknis

### 1. Sistem Logging (Pengganti Print)
Seluruh output terminal kini menggunakan modul `logging` bawaan Python dengan format waktu yang presisi:
Format: `%(asctime)s %(levelname)s - %(name)s - %(message)s`

Penerapan Level Log:
- **INFO:** Digunakan untuk mencatat alur normal. Contoh: "Validasi SKS: OK".
- **WARNING:** Digunakan saat aturan bisnis dilanggar. Contoh: "Validasi Gagal: SKS melebihi batas".
- **ERROR:** Digunakan saat proses registrasi ditolak sepenuhnya.

### 2. Google Style Docstrings
Setiap Kelas, Interface, dan Method dilengkapi dokumentasi standar industri dengan format Google Style.
- **Args:** Menjelaskan tipe data parameter input.
- **Returns:** Menjelaskan nilai kembalian fungsi.
- **Description:** Penjelasan singkat tujuan fungsi.
