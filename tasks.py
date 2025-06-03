from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Literal
from datetime import datetime
from model import Task, TaskCreate, TaskUpdate, StatusEnum
from crud import load_tasks, save_tasks

router = APIRouter()

tasks = load_tasks()
task_id_counter = max([t.id for t in tasks], default=0) + 1

@router.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global task_id_counter, tasks
    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=StatusEnum.pending,
        created_at=datetime.utcnow()
    )
    tasks.append(new_task)
    task_id_counter += 1
    save_tasks(tasks)
    return new_task

@router.get("/tasks/", response_model=List[Task])
def list_tasks(
    status: Optional[StatusEnum] = Query(None, description="Lọc theo trạng thái task"),
    sort_priority: Optional[Literal["asc", "desc"]] = Query(None, description="Sắp xếp theo priority"),
    limit: Optional[int] = Query(10, ge=1, description="Số lượng task trả về"),
    offset: Optional[int] = Query(0, ge=0, description="Bỏ qua số lượng task đầu")
):
    filtered_tasks = tasks
    if status:
        filtered_tasks = [t for t in filtered_tasks if t.status == status]
    if sort_priority == "asc":
        filtered_tasks.sort(key=lambda t: t.priority)
    elif sort_priority == "desc":
        filtered_tasks.sort(key=lambda t: t.priority, reverse=True)
    return filtered_tasks[offset: offset + limit]

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    global tasks
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[index] = updated_task
            save_tasks(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            save_tasks(tasks)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
