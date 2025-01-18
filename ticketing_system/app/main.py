from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from app.database import Base
from app.db_connection import (
  AsyncSessionLocal,
  get_db_session,
  get_engine
)
from pydantic import BaseModel, Field
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.operations import (
  create_ticket,
  get_ticket,
  update_ticket_price,
  delete_ticket
)

@asynccontextmanager
async def lifespan(app:FastAPI):
  engine = get_engine()
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
    yield
  await engine.dispose()

app = FastAPI(lifespan=lifespan)

class TicketRequest(BaseModel):
  price:float | None
  show: str | None
  user: str | None = None

@app.post("/tickets", response_model=dict[str, int])
async def create_ticket_route(
  ticket: TicketRequest,
  db_session: Annotated[AsyncSession, Depends(get_db_session)]):
  ticket_id = await create_ticket(
    db_session,
    ticket.show,
    ticket.user,
    ticket.price
  )
  return {"ticket_id": ticket_id}

@app.get("/tickets/{ticket_id}")
async def read_ticket(
  db_session: Annotated[AsyncSession, Depends(get_db_session)],
  ticket_id: int
):
  ticket = await get_ticket(db_session, ticket_id)
  if ticket is None:
    raise HTTPException(status_code=404, detail="Ticket not found")
  
  return ticket


class TicketDetailsUpdateRequest(BaseModel):
  seat: str | None = None
  ticket_type: str | None = None

class TicketUpdateRequest(BaseModel):
  price: float | None = Field(None, ge=0)

@app.put("/tickets/{ticket_id}")
async def update_ticket_route(
  ticket_id: int,
  ticket_update: TicketUpdateRequest,
  db_session: Annotated[AsyncSession, Depends(get_db_session)],
):
  update_dict_args = ticket_update.model_dump(exclude_unset=True)

  updated = await update_ticket_price(
    db_session,
    ticket_id,
    new_price=update_dict_args.get("price")
  )

  if not updated:
    raise HTTPException(status_code=404, detail="Ticket not found")
  
  return {
    "detail": "Ticket updated successfully",
    "ticket_id": ticket_id
  }
  
@app.delete("/tickets/{ticket_id}")
async def remove_ticket(
  db_session: Annotated[AsyncSession, Depends(get_db_session)],
  ticket_id: int
):
  ticket = await delete_ticket(db_session, ticket_id)
  if not ticket:
    raise HTTPException(status_code=404, detail="Ticket not found")
  
  return {
    "detail": "Ticket removed successfully",
    "ticket_id": ticket_id
  }