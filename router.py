from typing import Annotated
from fastapi import APIRouter, Depends, status

from reposit import TaskRepository
from schemas import Task, TaskAdd, TaskId

router = APIRouter(
    prefix="/tasks"
)


@router.post("/", response_model=TaskId, status_code=status.HTTP_201_CREATED)
async def add_task(task: TaskAdd = Depends()) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return {"message": "Success", "task_id": task_id}


@router.get("/", response_model=list[Task])
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks
