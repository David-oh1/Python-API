from fastapi import FastAPI
import models
from database import engine
from routers import post, user, auth, vote
from pydantic import BaseSettings
from config import settings

class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username: str = "postgres"
    secret_key: str = "234ui2340892348"

settings = Settings()

settings.database_password

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}