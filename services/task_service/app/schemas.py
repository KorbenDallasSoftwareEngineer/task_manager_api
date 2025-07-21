from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class Config:
    orm_mode = True
