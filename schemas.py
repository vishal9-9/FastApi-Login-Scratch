from typing import Optional
from pydantic import BaseModel

class add_blog(BaseModel):
    title: str
    body: str

class show_blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class add_user(BaseModel):
    name: str
    password: str
    email: str

class auth_user(BaseModel):
    username: str
    password: str

class show_user(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True

class show_user_blog(BaseModel):
    name: str
    email: str
    blogs: show_blog
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str