from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Mapped, mapped_column


class UserBase(BaseModel):
    username: str
    foo: int
    bar: int


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int

