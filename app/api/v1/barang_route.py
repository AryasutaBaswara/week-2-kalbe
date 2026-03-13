from fastapi import APIRouter, Depends
from typing import List
from app.core.database import get_db
from app.services import barang_service
from app.models import barang_schema
from app.core.security import get_current_user

router = APIRouter()

async def get_valid_barang_owner(
    item_id: int, 
    db = Depends(get_db), 
    user = Depends(get_current_user)
):
    # Fungsi ini memusatkan validasi: Ada barangnya? Milik user ini?
    # Service get_satu_barang sudah kita buat untuk melempar error jika tidak valid
    barang = await barang_service.get_satu_barang(db, item_id, user.id)
    return barang

@router.get("/", response_model=List[barang_schema.BarangResponse])
def read_all(db = Depends(get_db), user = Depends(get_current_user)):
    return barang_service.get_semua_barang(db, user.id)

@router.post("/", response_model=barang_schema.BarangResponse, status_code=201)
def create(item: barang_schema.BarangCreate, db = Depends(get_db), user = Depends(get_current_user)):
    return barang_service.tambah_barang(db, item, user.id)

@router.get("/{item_id}", response_model=barang_schema.BarangResponse)
def read_one(db = Depends(get_db), barang = Depends(get_valid_barang_owner)):
    return barang_service.get_satu_barang(db, barang["id"], barang["user_id"])

@router.patch("/{item_id}", response_model=barang_schema.BarangResponse)
async def update(item: barang_schema.BarangUpdate, db = Depends(get_db), barang = Depends(get_valid_barang_owner)):
    return await barang_service.update_barang(db, barang["id"], item, barang["user.id"])

@router.delete("/{item_id}")
def delete(db = Depends(get_db), barang = Depends(get_valid_barang_owner)):
    return barang_service.hapus_barang(db, barang["id"], barang["user_id"])