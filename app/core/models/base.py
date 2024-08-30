from logging import config
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped

from ..config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)