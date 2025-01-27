from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import File as FileModel
from utils.file_utils import save_file

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Ops User login"}

@router.post("/upload-file")
def upload_file_endpoint(file: UploadFile = File(...), db: Session = Depends(get_db)):
    allowed_types = ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
                     "application/vnd.openxmlformats-officedocument.presentationml.presentation", 
                     "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    filepath = save_file(file)
    new_file = FileModel(filename=filepath)
    db.add(new_file)
    db.commit()
    return {"message": "File uploaded successfully"}
