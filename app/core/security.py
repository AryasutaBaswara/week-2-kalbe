from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.database import get_db
from app.core.exceptions import AuthError
from supabase import Client

security = HTTPBearer()

def get_current_user(res: HTTPAuthorizationCredentials = Depends(security), db: Client = Depends(get_db)):
    token = res.credentials
    try:
        user_res = db.auth.get_user(token)
        return user_res.user
    except Exception:
        raise AuthError("Sesi login berakhir atau token salah.")