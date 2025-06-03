from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    pending = "pending"
    done = "done"

class TaskCreate(BaseModel):
    title: str = Field(..., example="Learn FastAPI")
    description: Optional[str] = Field("", example="Build an API using FastAPI")
    priority: int = Field(..., ge=1, example=1)

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int] = Field(None, ge=1)
    status: Optional[StatusEnum]

class Task(TaskCreate):
    id: int
    status: StatusEnum
    created_at: datetime
