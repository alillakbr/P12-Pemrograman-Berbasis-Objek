import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

# --- KONFIGURASI LOGGING (Langkah 2) ---
# Mengatur agar log level INFO ke atas ditampilkan dengan format waktu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(name)s - %(message)s'
)
# Membuat logger spesifik
LOGGER = logging.getLogger('CheckoutSystem')

# --- DATA MODEL ---
@dataclass
class Order:
    """
    Entitas yang merepresentasikan data pesanan pelanggan.
    """
    customer_name: str
    total_price: float
    status: str = "open"

# --- ABSTRAKSI (INTERFACE) ---
class IPaymentProcessor(ABC):
    """
    Interface untuk semua prosesor pembayaran.
    """
    @abstractmethod
    def process(self, order: Order) -> bool:
        """
        Memproses pembayaran untuk pesanan yang diberikan.

        Args:
            order (Order): Objek pesanan yang akan dibayar.

        Returns:
            bool: True jika pembayaran berhasil, False jika gagal.
        """
        pass

class INotificationService(ABC):
    """
    Interface untuk layanan notifikasi.
    """
    @abstractmethod
    def send(self, order: Order):
        """
        Mengirim notifikasi terkait status pesanan.

        Args:
            order (Order): Objek pesanan tujuan notifikasi.
        """
        pass

# --- IMPLEMENTASI KONKRIT ---
class CreditCardProcessor(IPaymentProcessor):
    """Implementasi pembayaran menggunakan Kartu Kredit."""
    def process(self, order: Order) -> bool:
        # Menggunakan logging alih-alih print
        LOGGER.info(f"Payment: Memproses tagihan Rp{order.total_price} via Kartu Kredit.")
        return True

class EmailNotifier(INotificationService):
    """Implementasi notifikasi via Email."""
    def send(self, order: Order):
        LOGGER.info(f"Notif: Email konfirmasi dikirim ke pelanggan {order.customer_name}.")

# --- SERVICE (KOORDINATOR) DENGAN DOCSTRING & LOGGING ---
class CheckoutService:
    """
    Kelas high-level untuk mengkoordinasi proses transaksi pembayaran.
    Kelas ini memisahkan logika pembayaran dan notifikasi (memenuhi SRP).
    """
    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        """
        Menginisialisasi CheckoutService dengan dependensi yang diperlukan.

        Args:
            payment_processor (IPaymentProcessor): Implementasi interface pembayaran.
            notifier (INotificationService): Implementasi interface notifikasi.
        """
        self.payment_processor = payment_processor
        self.notifier = notifier

    def process_checkout(self, order: Order) -> bool:
        """
        Menjalankan proses checkout dan memvalidasi pembayaran.

        Args:
            order (Order): Objek pesanan yang akan diproses.

        Returns:
            bool: True jika checkout sukses, False jika gagal.
        """
        LOGGER.info(f"Memulai checkout untuk {order.customer_name}. Total: {order.total_price}")
        
        # Delegasi tugas
        success = self.payment_processor.process(order)
        
        if success:
            order.status = "paid"
            self.notifier.send(order)
            LOGGER.info("Checkout Sukses. Status pesanan: PAID.")
            return True
        else:
            LOGGER.error("Pembayaran gagal. Transaksi dibatalkan.")
            return False

# --- EKSEKUSI UTAMA ---
if __name__ == "__main__":
    # Skenario: Checkout Berhasil
    order1 = Order("Andi", 500000)
    cc_processor = CreditCardProcessor()
    email_service = EmailNotifier()
    
    service = CheckoutService(cc_processor, email_service)
    service.process_checkout(order1)