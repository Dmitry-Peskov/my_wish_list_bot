import datetime
from typing import TYPE_CHECKING
from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.types import BigInteger, String, DateTime

if TYPE_CHECKING:
    from .user import User


class Desire(BaseModel):
    __tablename__ = "desire"

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime,
                                                          nullable=False,
                                                          server_default=func.now())
    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True,
                                    index=True,
                                    unique=True,
                                    nullable=False)
    title: Mapped[str] = mapped_column(String(300),
                                       nullable=False)
    url: Mapped[str] = mapped_column(String(2083),
                                     nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.telegram_id",
                                                    ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="desires")

    def __repr__(self):
        return f"{self.__class__.__name__} (id={self.id}; title={self.title}; user={self.user_id})"
