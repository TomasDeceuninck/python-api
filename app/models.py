from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from .database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[String] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[String]  = mapped_column(String)
    is_active: Mapped[Boolean] = mapped_column(Boolean, default=True)

    games: Mapped[List["Game"]] = relationship("Game", back_populates="player")


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    player_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    player: Mapped[User] = relationship("User", back_populates="games")