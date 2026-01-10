from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["argon2"],deprecated = "auto")

def hash_password(password:str):
    return pwd_content.hash(password)

def verify_password(password:str,hashed_password:str) -> bool:
    return pwd_content.verify(password,hashed_password)