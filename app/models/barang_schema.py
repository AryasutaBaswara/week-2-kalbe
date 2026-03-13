from pydantic import BaseModel
from typing import Optional

# 1. Base: Field yang selalu ada di semua kondisi
class BarangBase(BaseModel):
    nama: str
    deskripsi: Optional[str] = None
    harga: float
    stok: int

class BarangResponse(BarangBase):
    id: int
    user_id: str
# 2. Create: Sama dengan Base (biasanya tanpa ID)
class BarangCreate(BarangBase):
    pass

# 3. Update: Semua jadi Optional (untuk PATCH)
class BarangUpdate(BaseModel):
    nama: Optional[str] = None
    deskripsi: Optional[str] = None
    harga: Optional[float] = None
    stok: Optional[int] = None

# 4. Response: Apa yang dikirim ke user (pasti ada ID)


    class Config:
        from_attributes = True
