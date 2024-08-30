from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)


class Person(Base):
    name: Mapped[str] = mapped_column(unique=True)
    age: Mapped[int]
    surname: Mapped[str] = mapped_column(unique=True)