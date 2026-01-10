from fastapi import FastAPI
from routes.users import router as user_route
from routes import auth

app = FastAPI()

app.include_router(user_route)
app.include_router(auth.router)