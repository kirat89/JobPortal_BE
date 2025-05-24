"""Application model for SQLAlchemy ORM."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .job import Job
    from .user import User

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Application(Base):
    """Application model for the job application system."""

    __tablename__ = "applications"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False
    )
    status: Mapped[str] = mapped_column(
        Enum("applied", "shortlisted", "rejected", "hired", name="application_statuses"),
        default="applied",
    )
    cover_letter: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    resume_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    applied_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    user: Mapped["User"] = relationship(back_populates="applications")
    job: Mapped["Job"] = relationship(back_populates="applications")
