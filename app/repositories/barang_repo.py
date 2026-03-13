from supabase import Client

def get_all(db: Client, user_id: str):
    return db.table("barang").select("*").eq("user_id", user_id).execute()

def get_by_id(db: Client, item_id: int):
    return db.table("barang").select("*").eq("id", item_id).execute()

def create(db: Client, data: dict):
    return db.table("barang").insert(data).execute()

def update(db: Client, item_id: int, data: dict):
    return db.table("barang").update(data).eq("id", item_id).execute()

def delete(db: Client, item_id: int):
    return db.table("barang").delete().eq("id", item_id).execute()