from jose import JWTError, jwt
from datetime import timedelta

from app import models
from .import schemas,database
from fastapi import Depends,status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import datetime
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# from app import schemas

#SECRET_KEY
#Algorithn
#Expriation time 

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy() 

    expire = datetime.datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt=jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
  
  try:
      
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    id: str = payload.get("employee_id")

    if id is None:
      raise credentials_exception
    token_data = schemas.TokenData(id=str(id))
  except JWTError as e: 
     
      raise credentials_exception
  
  return token_data
  

def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    

    token = verify_access_token(token, credentials_exception) 

    User = db.query(models.Employee).filter(models.Employee.id == token.id).first()
    return User

