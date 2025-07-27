from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: schemas.UserCreate, hashed_password: str):
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user
