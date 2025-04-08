from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from capybara_clicker.extensions import db
from capybara_clicker.models.clicker import ClickCounter


class User(db.Model, UserMixin):
    """User model"""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(256))
    clicker: Mapped[ClickCounter] = relationship(back_populates="user")

    def get_id(self) -> str:
        """User 'id' for flask-login"""
        return self.username
