from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import  Ticket
from app.operations import (
    create_ticket,
    delete_ticket,
    get_ticket,
    update_ticket_price,
)

SPECIAL_TICKET_ID = 1234

async def assert_tickets_table_is_empty(
    db_session: AsyncSession
):
  async with db_session as session:
    result = await session.execute(select(Ticket))

  assert result.all() == []

async def test_create_ticket(
    db_session_test
):
  await assert_tickets_table_is_empty(db_session_test)

  ticket_id = await create_ticket(
    db_session_test,
    "The Rolling Stones Concert",
    "John Doe",
    100.0
  )

  assert ticket_id == 1

  ticket = await get_ticket(db_session_test, ticket_id)

  assert ticket is not None
  assert ticket.price == 100.0
  assert ticket.show == "The Rolling Stones Concert"
  assert ticket.user == "John Doe"


async def test_get_ticket(
    db_session_test,
    add_special_ticket
):
  ticket = await get_ticket(db_session_test, SPECIAL_TICKET_ID)

  assert ticket.id == SPECIAL_TICKET_ID
  assert ticket.show == "Special Show"

async def test_delete_ticket(
    db_session_test,
    add_special_ticket
):
  assert(
    await delete_ticket(db_session_test, 111)
    is False
  ) # non existing ticket

  assert(
    await delete_ticket(db_session_test, SPECIAL_TICKET_ID)
    is True
  )

  await assert_tickets_table_is_empty(db_session_test)

async def test_update_ticket_price(
    db_session_test,
    add_special_ticket
):
  assert(
    await update_ticket_price(db_session_test, SPECIAL_TICKET_ID, 250.0)
    is True
  )

  ticket = await get_ticket(db_session_test, SPECIAL_TICKET_ID)

  assert ticket.price == 250.0

  assert(
    await update_ticket_price(db_session_test, 111, 250.0)
    is False
  ) # non existing ticket