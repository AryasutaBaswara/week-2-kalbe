class InventoryException(Exception):
    """Base exception untuk semua error di aplikasi kita"""
    def __init__(self, message: str, code: str = "BAD_REQUEST"):
        self.message = message
        self.code = code

class BarangNotFoundError(InventoryException):
    def __init__(self, item_id: int):
        super().__init__(
            message=f"Barang dengan ID {item_id} tidak ditemukan.",
            code="ITEM_NOT_FOUND"
        )

class HargaInvalidError(InventoryException):
    def __init__(self, harga: float):
        super().__init__(
            message=f"Harga {harga} tidak valid. Minimal 500 rupiah.",
            code="INVALID_PRICE"
        )

class AksesDitolakError(InventoryException):
    def __init__(self, detail: str = "Bukan pemilik data"):
        super().__init__(message=f"Akses Ditolak: {detail}", code="FORBIDDEN_ACCESS")

class AuthError(InventoryException):
    def __init__(self, message: str = "Token tidak valid"):
        super().__init__(message, "UNAUTHORIZED")

class DataDuplikatError(InventoryException):
    def __init__(self, detail: str):
        super().__init__(message=f"Data sudah ada: {detail}", code="DUPLICATE_DATA")