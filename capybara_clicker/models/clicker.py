from sqlalchemy.orm import Mapped, mapped_column
from capybara_clicker.extensions import db


class ClickCounter(db.Model):
    __tablename__ = "click_counter"
    id: Mapped[int] = mapped_column(primary_key=True)
    count: Mapped[int] = mapped_column(default=0, server_default="0")
