from jose import jwt,JWTError
from schemas import TokenData
from database import session
from models import Users

SECRET_KEY = "25e343bf10d72225c2ef8b5b39121f8054852b9d8de0a0262201d50d0957de14"

def create_token(data: dict):
    to_encode = data.copy()
    jwt_token = jwt.encode(to_encode,SECRET_KEY)
    return jwt_token

def verify_token(token: str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = email
        user = session.query(Users).filter(Users.email == token_data).first()
        return user
    except JWTError:
        raise credentials_exception
    
    