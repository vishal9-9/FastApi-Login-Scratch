from fastapi import APIRouter,Depends,HTTPException
from models import Users
from sqlalchemy.orm import Session
from database import get_db
from schemas import auth_user
from passhash import Hasher
from fastapi.security import OAuth2PasswordRequestForm
from tokens import create_token

router = APIRouter(
    tags = ["Authentication"]
)

@router.post('/Authentication')
def auth(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    username = db.query(Users).filter(Users.email == request.username).first()
    if not username:
        raise HTTPException(status_code = 404,detail = "Username Incorrect")
    password = Hasher.verify_hash(request.password , username.password)
    if not password:
        raise HTTPException(status_code = 404,detail = "Password Incorrect")
    token = create_token(data = {'sub': username.email})
    return {"access_token" : token , "token_type": "bearer"}