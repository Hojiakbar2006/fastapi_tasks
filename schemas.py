from typing import Optional
from pydantic import BaseModel


class TaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class Task(TaskAdd):
    id: Optional[int] = None

    class Config:
        # Example configuration
        orm_mode = True


class TaskId(BaseModel):
    ok: bool = True
    task_id: int
