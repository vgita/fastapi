from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1900, le=2100)

class BookResponse(BaseModel):
    title: str
    author: str