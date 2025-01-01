from fastapi import APIRouter, HTTPException
from models.task import Task, TaskWithId, UpdateTask
from repos.tasks_repo import (
  read_all_tasks,
  read_task, 
  create_task, 
  update_task, 
  remove_task)

router = APIRouter()

@router.get("/tasks", response_model=list[TaskWithId])
def get_tasks():
  tasks = read_all_tasks()
  return tasks

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