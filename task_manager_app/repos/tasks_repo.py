import csv
from typing import Optional
from models.task import Task, TaskWithId, TaskV2WithId

DATABASE_FILENAME = "tasks.csv"

column_fields = ["id", "title", "description", "status"]

def read_all_tasks() -> list[TaskWithId]:
   with open(DATABASE_FILENAME) as csv_file:
      reader = csv.DictReader(csv_file)

      return [TaskWithId(**row) for row in reader]
   
def read_all_tasks_v2() -> list[TaskV2WithId]:
    with open(DATABASE_FILENAME) as csv_file:
        reader = csv.DictReader(csv_file)

        return [TaskV2WithId(**row) for row in reader]
   
def read_task(task_id:int) -> Optional[TaskWithId]:
    with open(DATABASE_FILENAME) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if int(row["id"]) == task_id:
                return TaskWithId(**row)
            
def create_task(task: Task) -> TaskWithId:
    task_id = get_next_id()
    task_with_id = TaskWithId(id=task_id, **task.model_dump())
    write_task_into_csv(task_with_id)
    return task_with_id

def update_task(id: int, task: dict) -> Optional[TaskWithId]:
    updated_task: Optional[TaskWithId] = None
    tasks = read_all_tasks()
    for number, task_ in enumerate(tasks):
        if task_.id == id:
            tasks[number] = (updated_task) = task_.model_copy(update = task)

    with open(DATABASE_FILENAME, mode="w", newline="\n") as csv_file: #rewrite the file
        writer = csv.DictWriter(csv_file, fieldnames=column_fields)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task.model_dump())
    
    if updated_task:
        return updated_task

def remove_task(id: int) -> Optional[Task]:
    deleted_task: Optional[Task] = None
    tasks = read_all_tasks()
    with open(DATABASE_FILENAME, mode="w", newline="\n") as csv_file: #rewrite the file
        writer = csv.DictWriter(csv_file, fieldnames=column_fields)
        writer.writeheader()
        for task in tasks:
            if task.id == id:
                deleted_task = task
                continue
            writer.writerow(task.model_dump())
        
        if deleted_task:
            dict_task_without_id = (deleted_task.model_dump())
            del dict_task_without_id["id"]
            return Task(**dict_task_without_id)

def write_task_into_csv(task: TaskWithId):
    with open(DATABASE_FILENAME, mode="a", newline="\n") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_fields)
        writer.writerow(task.model_dump())
            
def get_next_id() -> int:
    try:
        with open(DATABASE_FILENAME, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            max_id = max([int(row["id"]) for row in reader])
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1