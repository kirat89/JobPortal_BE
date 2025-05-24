"""Location model for SQLAlchemy ORM."""

import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Location(Base):
    """Location model for the application."""

    __tablename__ = "locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    city = Column(String, nullable=False)
    state = Column(String)
    country = Column(String)
    timezone = Column(String)
