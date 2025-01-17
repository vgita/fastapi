import uvicorn

if __name__ == "__main__":
    uvicorn.run("protoapp.main:app", reload=True)