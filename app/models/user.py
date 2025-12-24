from typing import List
from datetime import datetime, timezone
from uuid import uuid4, UUID
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy.types import Uuid


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[Uuid] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4
    )
    email: Mapped[str] = mapped_column(String(50))
    password_salt: Mapped[str]
    password_hash: Mapped[str]
    
    def __repr__(self) -> str:
        return f"<user email={self.email}>"
    