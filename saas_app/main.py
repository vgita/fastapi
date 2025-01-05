from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
from db_connection import get_engine, get_session
from operations import add_user
from models.base import Base
from models.user import (
    ResponseCreateUser, 
    UserCreateResponse,
    UserCreateBody,
)
from security import router as security_router
from rbac import router as rbac_router
from premium_access import router as premium_router
from github_login import router as github_router
from third_party_login import resolve_github_token

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=get_engine())
    yield


app = FastAPI(
    title="Saas application", lifespan=lifespan
)

app.include_router(security_router)
app.include_router(rbac_router)
app.include_router(premium_router)
app.include_router(github_router)


@app.post("/register/user", 
          status_code= status.HTTP_201_CREATED,
          response_model=ResponseCreateUser,
          responses= {
              status.HTTP_409_CONFLICT: {
                  "description": "User already exists"
              }
          })
def register(
    user: UserCreateBody,
    session: Session = Depends(get_session)
) -> dict[str, UserCreateResponse]:
    user = add_user(session=session, **user.model_dump())
    if not user:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "User already exists"
        )
    user_response = UserCreateResponse(
        username=user.username,
        email=user.email
    )
    return {
        "message": "User created",
        "user": user_response
    }

@app.get(
    "/home",
    responses={
        status.HTTP_403_FORBIDDEN: {
            "description": "token not valid"
        }
    },
)
def homepage(
    user: UserCreateResponse = Depends(
        resolve_github_token
    ),
):
    return {"message": f"logged in {user.username} !"}