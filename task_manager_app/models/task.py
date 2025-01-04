from pydantic import BaseModel

class Task(BaseModel):
  title: str
  description: str
  status: str

class TaskWithId(Task):
  id: int

class TaskV2(BaseModel):
  title: str
  description:str
  status: str
  priority: str | None = "lower"

class TaskV2WithId(TaskV2):
  id: int

class UpdateTask(BaseModel):
  title: str | None = None
  description: str | None = None
  status: str | None = None