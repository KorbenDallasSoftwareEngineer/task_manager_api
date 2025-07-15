from dotenv import load_dotenv
import os
from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="Auth Service")

app.include_router(router)


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
