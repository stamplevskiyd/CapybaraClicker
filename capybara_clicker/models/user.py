from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from capybara_clicker.extensions import db
from capybara_clicker.models.clicker import ClickCounter


class User(db.Model):
    """User model"""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    clicker: Mapped[ClickCounter] = relationship(back_populates="user")
