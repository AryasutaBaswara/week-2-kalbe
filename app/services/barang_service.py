from supabase import Client
from app.core.exceptions import BarangNotFoundError, HargaInvalidError, DataDuplikatError, AksesDitolakError
from app.repositories import barang_repo
from app.models import barang_schema

def get_semua_barang(db: Client, user_id: str):
    res = barang_repo.get_all(db, user_id)
    return res.data

def get_satu_barang(db: Client, item_id: int, user_id: str):
    res = barang_repo.get_by_id(db, item_id)
    if not res.data:
        raise BarangNotFoundError(item_id)
    
    barang = res.data[0]
    if barang["user_id"] != user_id:
        raise AksesDitolakError(f"Barang ID {item_id} bukan milik Anda")
        
    return barang

def tambah_barang(db: Client, item: barang_schema.BarangCreate, user_id: str):
    if item.harga < 500:
        raise HargaInvalidError(item.harga)
    
    check = db.table("barang").select("*").eq("nama", item.nama).eq("user_id", user_id).execute()
    if check.data:
        raise DataDuplikatError(item.nama)
    
    payload = item.model_dump()
    payload["user_id"] = user_id

    res = barang_repo.create(db, payload)
    return res.data[0]

async def tambah_barang_rpc(db: Client, item: barang_schema.BarangCreate, user_id: str):
    # Nama di sini HARUS SAMA dengan "Name of function" di dashboard
    res = db.rpc("tambah_barang_aman", {
        "p_nama": item.nama,
        "p_deskripsi": item.deskripsi,
        "p_harga": item.harga,
        "p_stok": item.stok,
        "p_user_id": user_id
    }).execute()
    return res.data

def update_barang(db: Client, item_id: int, item: barang_schema.BarangUpdate, user_id: str):
    get_satu_barang(db, item_id, user_id) # Cek keberadaan
    update_data = item.model_dump(exclude_unset=True)
    res = barang_repo.update(db, item_id, update_data)
    return res.data[0]

def hapus_barang(db: Client, item_id: int, user_id: str):
    get_satu_barang(db, item_id, user_id)
    barang_repo.delete(db, item_id)
    return {"message": "Berhasil dihapus"}