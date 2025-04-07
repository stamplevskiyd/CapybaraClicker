from sqlalchemy.orm import Mapped, mapped_column
from app import db


class ClickCounter(db.Model):
    __tablename__ = "click_counter"
    id: Mapped[int] = mapped_column(primary_key=True)
    count: Mapped[int] = mapped_column(default=0, server_default="0")


# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     email: Mapped[str]
