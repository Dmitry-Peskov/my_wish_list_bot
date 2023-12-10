from typing import TYPE_CHECKING, List
from datetime import datetime
from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey
from sqlalchemy.types import BigInteger, String, DateTime

if TYPE_CHECKING:
    from .user import User


class ActionLogDB(BaseModel):
    __tablename__ = "db_action_log"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True,
                                    index=True,
                                    unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 nullable=False,
                                                 default=datetime.now(),
                                                 server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.telegram_id",
                                                    ondelete="CASCADE"))

    message: Mapped[str] = mapped_column(String,
                                         nullable=False,
                                         index=True)
    details: Mapped[str | None] = mapped_column(String,
                                                nullable=True)

    user: Mapped["User"] = relationship(back_populates="db_action_log")

    def __repr__(self):
        return f"| {self.created_at} ; {self.user_id} ; {self.message} ; {self.details} |"