from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.done as done_schema
import api.cruds.done as done_cruds
from api.db import get_db

router = APIRouter()

@router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_cruds.get_done(db, task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400, detail="Done already exists")

    return await done_cruds.create_done(db, task_id)


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_cruds.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Done is not founded")

    return await done_cruds.delete_done(db, original=done)