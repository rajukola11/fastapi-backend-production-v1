from fastapi import APIRouter,status,Depends,HTTPException
from schemas.user import UserCreate,UserResponse
from sqlalchemy.orm import Session
from models.user import User
from database import get_db
from utilis.user import hash_password

router = APIRouter()

@router.get("/users/{user_id}/" , response_model=UserResponse,status_code=status.HTTP_200_OK)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.post("/users/",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db:Session=Depends(get_db)):
    hashed = hash_password(user.password)
    new_user = User(name = user.name,hashed_password = hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

