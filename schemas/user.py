from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    name:str
    password:str=Field(min_length=6,max_length=70)

class UserResponse(BaseModel):
    id : int
    name : str

    class Config:
        orm_mode = True

class UserVerify(BaseModel):
    name:str
    password:str=Field(min_length=6,max_length=70)