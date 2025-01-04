from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.security import User, UserInDB
from repos.security import (
  fake_token_generator,
  fakely_hash_password,
  fake_users_db,
  get_user_from_token
)

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
  user_dict = fake_users_db.get(form_data.username)
  if not user_dict:
    raise HTTPException(status_code=400, detail="Incorrect username or password")
  
  user = UserInDB(**user_dict)
  hashed_password = fakely_hash_password(form_data.password)
  if not hashed_password == user.hashed_password:
    raise HTTPException(status_code=400, detail="Incorrect username or password")
  token = fake_token_generator(user)
  return {"access_token": token, "token_type": "bearer"}

@router.get("/users/me")
def read_users_me(current_user: User = Depends(get_user_from_token)):
  return current_user

