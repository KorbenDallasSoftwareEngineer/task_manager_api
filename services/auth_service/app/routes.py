from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import models, schemas, auth
from app.database import get_db
from app.auth import verify_password, create_access_token, get_current_user
from app.schemas import UserLogin
from app import crud


router = APIRouter()


@router.post('/register', response_model=schemas.UserResponse)
async def register_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем есть ли юзер
    existing_user = await crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Хешируем пароль и сохраняем юзера
    new_user = await crud.create_user(db, user, auth.hash_password(user.password))
    return new_user


@router.post('/login')
async def login(user: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    # Ищем юзера по почте
    db_user = await crud.get_user_by_email(db, user.email)

    # Проверяем пароль
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=401, detail="Invalid email or password")

    # Генерируем токен
    token = auth.create_access_token({'sub': db_user.email})

    return {"access_token": token, "token_type": 'bearer'}


@router.get('/me', response_model=schemas.UserResponse)
async def get_me(current_user: models.User = Depends(get_current_user)):
    return current_user
