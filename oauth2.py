from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
import tokens

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'Authentication')

def current_user(token:str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Unauthorized",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    return tokens.verify_token(token, credential_exception)