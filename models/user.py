import datetime
from typing import TYPE_CHECKING, List
from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from sqlalchemy.types import BigInteger, String, DateTime

if TYPE_CHECKING:
    from .desire import Desire


class User(BaseModel):
    __tablename__ = "user"

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime,
                                                          nullable=False,
                                                          server_default=func.now())
    telegram_id: Mapped[int] = mapped_column(BigInteger,
                                             primary_key=True,
                                             unique=True,
                                             nullable=False,
                                             index=True)
    fullname: Mapped[str | None] = mapped_column(String(100),
                                                 nullable=True)
    nickname: Mapped[str | None] = mapped_column(String(100),
                                                 nullable=True)

    desires: Mapped[List["Desire"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"{self.__class__.__name__} (id={self.telegram_id}; fullname={self.fullname}; nickname={self.nickname})"
