from fastapi import APIRouter
from models.book import BookCreate, BookResponse

router = APIRouter()

@router.get("/books", response_model=list[BookResponse])
async def read_books(year:int = None):
    return [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F.Scott Fitzgerald"
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell"
        }
    ]

@router.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F.Scott Fitzgerald"
      }

@router.post("/books")
async def create_book(book: BookCreate):
    return book