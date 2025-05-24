"""Company model for SQLAlchemy ORM."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from .job import Job
    from .user import User

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Company(Base):
    """Company model for the application."""

    __tablename__ = "companies"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    subdomain: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    jobs: Mapped[List["Job"]] = relationship(back_populates="company")
    owner: Mapped["User"] = relationship(back_populates="companies")
