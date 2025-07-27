from app.routes import router
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


app = FastAPI(title="Auth Service")
app.include_router(router)
