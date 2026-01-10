from fastapi import APIRouter,Depends,HTTPException
from schemas.user import UserVerify
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from utilis.user import verify_password
from utilis.jwt import create_access_token,get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login",tags=["auth"])
def verify_login(user_verify:UserVerify,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.name == user_verify.name).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    if not verify_password(user_verify.password,user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )
    access_token = create_access_token(
        data={"sub":user.name,"user_id":user.id}
    )
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

@router.get("/me")
def read_me(current_user : User=Depends(get_current_user)):
    return {
        "id":current_user.id,
        "name":current_user.name
    }
    