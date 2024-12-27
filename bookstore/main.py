import json
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse
from routes.authors import router as authors_router
from routes.books import router as books_router

app = FastAPI()

app.include_router(authors_router)
app.include_router(books_router)


@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=404, detail="Not Found")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops! Something went wrong!"},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse("Some plain text response:"
                             f"\n{json.dumps(exc.errors(), indent=2)}",
                             status_code=status.HTTP_400_BAD_REQUEST)

