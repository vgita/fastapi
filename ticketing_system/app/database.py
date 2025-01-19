from sqlalchemy import (
  Column, 
  Float, 
  ForeignKey, 
  Table,
  ForeignKey
)
from sqlalchemy.orm import (
  DeclarativeBase,
  Mapped,
  mapped_column,
  relationship
)

class Base(DeclarativeBase):
  pass

class Sponsor(Base):
  __tablename__ = 'sponsors'
  id:Mapped[int] = mapped_column(primary_key=True)
  name:Mapped[str] = mapped_column(unique=True)
  #many to many relationship with events
  events:Mapped[list["Event"]] = relationship(
    secondary="sponsorships",
    back_populates="sponsors"
  )

#association table for many to many relationship between events and sponsors
class Sponsorship(Base):
  __tablename__ = 'sponsorships'
  event_id:Mapped[int] = mapped_column(
    ForeignKey("events.id"),
    primary_key=True
  )
  sponsor_id:Mapped[int] = mapped_column(
    ForeignKey("sponsors.id"),
    primary_key=True
  )
  amount:Mapped[float] = mapped_column(
    nullable=False,
    default=10
  )

class Event(Base):
  __tablename__ = 'events'
  id:Mapped[int] = mapped_column(primary_key=True)
  name:Mapped[str]
  #one to many relationship with tickets
  tickets:Mapped[list["Ticket"]] = relationship(
    back_populates="event"
  )
  #many to many relations with sponsors
  sponsors:Mapped[list["Sponsor"]] = relationship(
    secondary="sponsorships",
    back_populates="events"
  )

class Ticket(Base):
  __tablename__ = 'tickets'
  id:Mapped[int] = mapped_column(primary_key=True)
  price: Mapped[float]=mapped_column(nullable=True)
  show:Mapped[str|None]
  user:Mapped[str|None]
  sold:Mapped[bool]=mapped_column(default=False)
  details:Mapped["TicketDetails"] = relationship(
    back_populates="ticket"
  )
  event_id:Mapped[int|None] = mapped_column(
    ForeignKey("events.id")
  )
  #on to many relationship with events
  event:Mapped["Event|None"] = relationship(
    back_populates="tickets"
  )

class TicketDetails(Base):
  __tablename__="ticket_details"
  id:Mapped[int]=mapped_column(primary_key=True)

  #one to one relationship with ticket
  ticket_id:Mapped[int]=mapped_column(
    ForeignKey("tickets.id")
  )
  ticket:Mapped[Ticket]=relationship(
    back_populates="details"
  )
  seat:Mapped[str|None]
  ticket_type:Mapped[str|None]