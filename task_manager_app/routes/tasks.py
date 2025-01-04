from typing import Optional
from fastapi import APIRouter, HTTPException
from models.task import Task, TaskWithId, UpdateTask, TaskV2WithId
from repos.tasks_repo import (
  read_all_tasks,
  read_all_tasks_v2,
  read_task, 
  create_task, 
  update_task, 
  remove_task)

router = APIRouter()

@router.get("/tasks", response_model=list[TaskWithId])
def get_tasks(
    status: Optional[str] = None,
    title: Optional[str] = None
  ):
  tasks = read_all_tasks()

  if status:
    tasks = [task for task in tasks if task.status == status]
  if title:
    tasks = [task for task in tasks if title.lower() in task.title.lower()]

  return tasks

@router.get("/v2/tasks", response_model=list[TaskV2WithId])
def get_tasks_v2():
  tasks = read_all_tasks_v2()
  return tasks

@router.get("/tasks/search", response_model=list[TaskWithId])
def search_tasks(keyword: str):
  tasks = read_all_tasks()

  filtered_tasks = [task for task in tasks if keyword.lower() in (task.title + task.description).lower()]
    
  return filtered_tasks

@router.get("/tasks/{task_id}", response_model=TaskWithId)
def get_task(task_id: int):
  task = read_task(task_id)
  if task is None:
    raise HTTPException(status_code=404, detail="Task not found")
  return task

@router.post("/tasks", response_model=TaskWithId)
def add_task(task:Task):
  return create_task(task)

@router.put("/tasks/{task_id}", response_model=TaskWithId)
def update(task_id: int, task_update: UpdateTask):
  updated = update_task(task_id, task_update.model_dump(exclude_unset=True))
  if not updated:
    raise HTTPException(status_code=404, detail="Task not found")
  return updated

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
  deleted = remove_task(task_id)
  if not deleted:
    raise HTTPException(status_code=404, detail="Task not found")
  return deleted