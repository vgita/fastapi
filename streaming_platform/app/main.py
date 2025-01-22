from fastapi import (
  HTTPException,
  FastAPI
)
from contextlib import asynccontextmanager
from app.db_connection import (
  ping_mongo_db_server
)
from bson import ObjectId
from fastapi import Body, Depends
from app.database import mongo_database
from fastapi.encoders import ENCODERS_BY_TYPE

ENCODERS_BY_TYPE[ObjectId] = str

@asynccontextmanager
async def lifespan(app:FastAPI):
  await ping_mongo_db_server()
  yield

app = FastAPI(lifespan=lifespan)

@app.post("/songs")
async def add_song(
  song: dict = Body(example={
    "title":"My Song",
    "artist":"My Artist",
    "genre":"My Genre"
  }),
  mongo_db=Depends(mongo_database)
):
  await mongo_db.songs.insert_one(song)
  return {
    "message":"Song added successfully",
    "id":song["_id"]
  }

@app.get("/song/{song_id}")
async def get_song(
    song_id: str,
    db=Depends(mongo_database),
):
  song = await db.songs.find_one(
      {
          "_id": ObjectId(song_id)
          if ObjectId.is_valid(song_id)
          else None
      }
  )
  if not song:
      raise HTTPException(
          status_code=404, detail="Song not found"
      )
  return song

@app.put("/song/{song_id}")
async def update_song(
    song_id: str,
    updated_song: dict,
    db=Depends(mongo_database),
):
    result = await db.songs.update_one(
        {
            "_id": ObjectId(song_id)
            if ObjectId.is_valid(song_id)
            else None
        },
        {"$set": updated_song},
    )
    if result.modified_count == 1:
        return {"message": "Song updated successfully"}

    raise HTTPException(
        status_code=404, detail="Song not found"
    )

@app.delete("/song/{song_id}")
async def delete_song(
    song_id: str,
    db=Depends(mongo_database),
):
    result = await db.songs.delete_one(
        {
            "_id": ObjectId(song_id)
            if ObjectId.is_valid(song_id)
            else None
        }
    )
    if result.deleted_count == 1:
        return {"message": "Song deleted successfully"}

    raise HTTPException(
        status_code=404, detail="Song not found"
    )