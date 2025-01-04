from fastapi import FastAPI
from routes.tasks import router as tasks_router
from routes.security import router as security_router
from fastapi.openapi.utils import get_openapi

app = FastAPI(
  title="Task Manager API",
  description="A simple API to manage tasks",
  version="0.1.0"
)

app.include_router(tasks_router)
app.include_router(security_router)

def custom_openapi():
  if app.openapi_schema:
    return app.openapi_schema
  openapi_schema = get_openapi(
    title="Customized Title",
    version="2.0.0",
    description="This is a very custom OpenAPI schema",
    routes=app.routes
  )
  del openapi_schema["paths"]["/token"]
  app.openapi_schema = openapi_schema
  return app.openapi_schema

app.openapi = custom_openapi
