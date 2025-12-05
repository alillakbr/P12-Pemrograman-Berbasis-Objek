import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

# --- 1. KONFIGURASI LOGGING ---
# Sesuai Modul Hal 3: Format logging menampilkan Waktu, Level, Nama Logger, dan Pesan [cite: 54]
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(name)s - %(message)s'
)
LOGGER = logging.getLogger('RegistrasiSystem')

# --- DATA MODEL ---
@dataclass
class Student:
    """
    Data Class yang menyimpan informasi mahasiswa.
    """
    name: str
    sks_taken: int
    prerequisites_met: bool

# --- ABSTRAKSI ---
class IValidationRule(ABC):
    """
    Interface (Kontrak) untuk semua aturan validasi registrasi.
    """
    @abstractmethod
    def validate(self, student: Student) -> bool:
        """
        Memvalidasi data mahasiswa berdasarkan aturan tertentu.

        Args:
            student (Student): Objek mahasiswa yang akan divalidasi.

        Returns:
            bool: True jika validasi lolos, False jika gagal.
        """
        pass

# --- IMPLEMENTASI RULE (LOGGING DIGANTI) ---
class SksLimitRule(IValidationRule):
    """Aturan untuk mengecek batas maksimal SKS."""
    
    def validate(self, student: Student) -> bool:
        if student.sks_taken > 24:
            # Menggunakan WARNING untuk kegagalan validasi
            LOGGER.warning(f"Validasi Gagal: {student.name} mengambil {student.sks_taken} SKS (Maks 24).")
            return False
        LOGGER.info("Validasi SKS: OK.")
        return True

class PrerequisiteRule(IValidationRule):
    """Aturan untuk mengecek pemenuhan mata kuliah prasyarat."""
    
    def validate(self, student: Student) -> bool:
        if not student.prerequisites_met:
            LOGGER.warning(f"Validasi Gagal: {student.name} belum memenuhi prasyarat.")
            return False
        LOGGER.info("Validasi Prasyarat: OK.")
        return True

class JadwalBentrokRule(IValidationRule):
    """Aturan baru (Challenge) untuk mengecek bentrok jadwal."""
    
    def validate(self, student: Student) -> bool:
        # Simulasi logika
        LOGGER.info("Validasi Jadwal: Mengecek jadwal... Tidak ada bentrok.")
        return True

# --- SERVICE (DOKUMENTASI & LOGGING) ---
class RegistrationService:
    """
    Kelas koordinator yang menangani proses registrasi mahasiswa.
    Menerapkan prinsip SRP dengan mendelegasikan validasi ke rules.
    """
    
    def __init__(self, rules: list[IValidationRule]):
        """
        Menginisialisasi service dengan daftar aturan validasi.

        Args:
            rules (list[IValidationRule]): Daftar objek aturan yang mengimplementasikan IValidationRule.
        """
        self.rules = rules

    def register_student(self, student: Student) -> bool:
        """
        Menjalankan serangkaian validasi untuk meregistrasi mahasiswa.

        Args:
            student (Student): Data mahasiswa yang mendaftar.

        Returns:
            bool: True jika semua validasi sukses, False jika ada satu saja yang gagal.
        """
        LOGGER.info(f"--- Memulai Registrasi untuk {student.name} ---")
        
        for rule in self.rules:
            # Jika salah satu rule gagal (return False), proses berhenti
            if not rule.validate(student):
                LOGGER.error("Registrasi DITOLAK karena validasi gagal.\n")
                return False
        
        LOGGER.info("Registrasi DITERIMA. Semua persyaratan terpenuhi.\n")
        return True

# --- EKSEKUSI ---
if __name__ == "__main__":
    # Skenario 1: Mahasiswa Lolos (Budi)
    maba = Student("Budi", 20, True)
    
    # Setup Rules (Dependency Injection)
    rules_list = [
        SksLimitRule(),
        PrerequisiteRule(),
        JadwalBentrokRule()
    ]
    
    service = RegistrationService(rules_list)
    service.register_student(maba)

    # Skenario 2: Mahasiswa Gagal (Siti - SKS Berlebih)
    siti = Student("Siti", 25, True)
    service.register_student(siti)