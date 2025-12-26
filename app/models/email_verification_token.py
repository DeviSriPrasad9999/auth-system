from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

class EmailVerificationToken(Base):
    __tablename__ = "email_verification_token"

    id: Mapped[int] = mapped_column(primary_key=True)

    token: Mapped[str] = mapped_column(String,unique=True, index=True)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True)
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship("User",back_populates="email_verification_tokens")
