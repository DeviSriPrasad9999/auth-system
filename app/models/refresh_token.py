from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import Boolean, DateTime, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(String, unique=True, index=True)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    revoked: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    user = relationship("User", backref="refresh_tokens")
    