from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Auth Service")

app.include_router(router)
