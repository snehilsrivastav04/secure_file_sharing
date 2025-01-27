from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, File
from auth import hash_password, create_access_token
from utils.email_utils import send_verification_email

router = APIRouter()

@router.post("/signup")
def signup(email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = hash_password(password)
    new_user = User(email=email, hashed_password=hashed_password, is_verified=False)
    db.add(new_user)
    db.commit()
    token = create_access_token({"sub": email})
    send_verification_email(email, token)
    return {"message": "Signup successful, check your email for verification"}

@router.get("/download-file/{file_id}")
def download_file(file_id: int, db: Session = Depends(get_db)):
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return {"download-link": f"http://example.com/download/{file.filename}"}
