from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    is_ops_user: bool

class FileResponse(BaseModel):
    id: int
    filename: str
