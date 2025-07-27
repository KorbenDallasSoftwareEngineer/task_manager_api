from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, crud
from app.database import get_db
from app.auth import verify_token

router = APIRouter()


@router.post('/tasks', response_model=schemas.TaskResponse)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_task(db, task)


@router.get('/tasks', response_model=list[schemas.TaskResponse])
async def read_tasks(db: AsyncSession = Depends(get_db), user_id: str = Depends(verify_token)):
    return await crud.get_tasks(db)


@router.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify_token)):
    task = await crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
async def update_task_endpoint(task_id: int, task_update: schemas.TaskUpdate,
                               db: AsyncSession = Depends(get_db), user_id: str = Depends(verify_token)):
    task = await crud.update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify_token)):
    task = await crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
