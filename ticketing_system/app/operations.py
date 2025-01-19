from sqlalchemy import (
  update,
  delete
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import Ticket, TicketDetails
from typing import Optional

async def create_ticket(
    db_session: AsyncSession,
    show_name: str,
    user: Optional[str] = None,
    price: Optional[float] = None,
) -> int:
    """
    Create a new ticket for a show.

    Args:
        db_session (AsyncSession): The async database session.
        show_name (str): The name of the show.
        user (Optional[str]): The user purchasing the ticket.
        price (Optional[float]): The price of the ticket.

    Returns:
        int: The ID of the created ticket.
    """
    ticket = Ticket(
        show=show_name,
        user=user,
        price=price,
        details=TicketDetails()
    )
    async with db_session.begin():
        db_session.add(ticket)
        await db_session.flush()  # Flush to get the ticket ID
        ticket_id = ticket.id
        #await db_session.commit() REDUNDANT

    return ticket_id

async def get_ticket(
  db_session: AsyncSession,
  ticket_id: int
) -> Ticket | None:
  """
  Get a ticket by its ID.

  Args:
    db_session (AsyncSession): The async database session.
    ticket_id (int): The ID of the ticket.

  Returns:
    Ticket | None: The ticket, if found.
  """
  query = select(Ticket).where(Ticket.id == ticket_id)

  async with db_session as session:
    tickets = await session.execute(query)
    return tickets.scalars().first()
  
async def update_ticket_price(
  db_session: AsyncSession,
  ticket_id: int,
  new_price: float
) -> bool:
  """
  Update the price of a ticket.

  Args:
    db_session (AsyncSession): The async database session.
    ticket_id (int): The ID of the ticket.
    new_price (float): The new price of the ticket.

  Returns:
    bool: True if the ticket was updated successfully.
  """
  query = (
    update(Ticket)
    .where(Ticket.id == ticket_id)
    .values(price=new_price)
  )

  async with db_session as session:
     ticket_updated = await session.execute(query)
     await session.commit()

     if ticket_updated.rowcount == 1:
       return True
     return False
  
async def delete_ticket(
  db_session: AsyncSession,
  ticket_id: int
) -> bool:
  """
  Delete a ticket by its ID.

  Args:
    db_session (AsyncSession): The async database session.
    ticket_id (int): The ID of the ticket.

  Returns:
    bool: True if the ticket was deleted successfully.
  """
  async with db_session as session:
    tickets_removed = await session.execute(
       delete(Ticket).where(Ticket.id == ticket_id)
    )
    await session.commit()

    if tickets_removed.rowcount == 0:
      return False
    return True
  
async def update_ticket_details(
  db_session:AsyncSession,
  ticket_id:int,
  updating_details:dict
) -> bool:
    ticket_query = update(TicketDetails).where(
      TicketDetails.ticket_id == ticket_id)

    if updating_details != {}:
      ticket_query = ticket_query.values(**updating_details)

      result = await db_session.execute(ticket_query)

      await db_session.commit()

      if result.rowcount == 0:
        return False
      
    return True