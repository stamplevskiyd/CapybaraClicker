from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from capybara_clicker.extensions import db

if TYPE_CHECKING:
    from capybara_clicker.models.user import User


class ClickCounter(db.Model):
    __tablename__ = "click_counters"
    id: Mapped[int] = mapped_column(primary_key=True)
    count: Mapped[int] = mapped_column(default=0, server_default="0")
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    user: Mapped[Optional["User"]] = relationship(back_populates="clicker")
