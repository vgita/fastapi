from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker)

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    email: Mapped[str]

# create the tables in the database
Base.metadata.create_all(engine)

# establish a connection to the database
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
    )