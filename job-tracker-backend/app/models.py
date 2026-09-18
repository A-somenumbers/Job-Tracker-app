import enum
from datetime import date
from sqlalchemy import Column, Integer, String, Date, Enum, Text
from .database import Base


class StatusEnum(str, enum.Enum):
    applied = "applied"
    interviewing = "interviewing"
    offer = "offer"
    rejected = "rejected"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    industry = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.applied, nullable=False)
    date_applied = Column(Date, default=date.today, nullable=False)
    notes = Column(Text, nullable=True)
