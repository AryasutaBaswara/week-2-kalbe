from fastapi import APIRouter, Depends, HTTPException
from app.models.auth_schema import UserAuth
from app.core.database import get_db

router = APIRouter()

@router.post("/register")
def register(payload: UserAuth, db = Depends(get_db)):
    db.auth.sign_up(
        {
        "email": payload.email, 
        "password": payload.password
        })
    return {"message": "Cek email verifikasi!"}

@router.post("/login")
def login(payload: UserAuth, db = Depends(get_db)):
    try:
        res = db.auth.sign_in_with_password(
            {
             "email": payload.email, 
             "password": payload.password
            })
        return {"access_token": res.session.access_token, "token_type": "bearer"}
    except:
        raise HTTPException(status_code=400, detail="Login Gagal")