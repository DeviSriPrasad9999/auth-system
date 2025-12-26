from typing import List
from datetime import datetime, timezone
from uuid import uuid4, UUID
from sqlalchemy import ForeignKey, String, DateTime, func, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy.types import Uuid
from models.email_verification_token import EmailVerificationToken

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4
    )
    email: Mapped[str] = mapped_column(String(50))
    password_hash: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )
    email_verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    email_verification_tokens: Mapped[list["EmailVerificationToken"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<user email={self.email}>"
    