from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from models import Users
from schemas import add_user,show_user
from passhash import Hasher
from oauth2 import current_user,oauth2_scheme

router = APIRouter(
    tags = ["User"]
)

@router.post('/user')
def create_user(request: add_user,db: Session = Depends(get_db)):
    hashed_pass = Hasher.hash_pass(request.password)
    user = Users(name = request.name , password = hashed_pass, email = request.email)
    db.add(user)
    db.commit()
    db.close()
    return "User Created"

@router.get('/user/{id}',response_model = show_user)
def get_user_id(id: int, db: Session = Depends(get_db),user : show_user = Depends(current_user)):
    user = db.query(Users).filter(Users.id == id).first()
    return user

@router.post('/user/me',response_model = show_user)
def get_user_id(db: Session = Depends(get_db),user : show_user = Depends(current_user)):
    #user = db.query(Users).filter(Users.email == user.email).first()
    return user