import os
import json
from typing import List
from datetime import datetime
from model import Task, StatusEnum

DATA_FILE = "tasks_data.json"

def load_tasks() -> List[Task]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        tasks = []
        for item in data:
            item["created_at"] = datetime.fromisoformat(item["created_at"])
            item["status"] = StatusEnum(item["status"])
            tasks.append(Task(**item))
        return tasks

def save_tasks(tasks: List[Task]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        data = []
        for task in tasks:
            data.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "status": task.status.value,
                "created_at": task.created_at.isoformat()
            })
        json.dump(data, f, indent=4, ensure_ascii=False)
