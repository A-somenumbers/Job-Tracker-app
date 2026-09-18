from datetime import date
from typing import Optional
from pydantic import BaseModel
from .models import StatusEnum


class ApplicationBase(BaseModel):
    company: str
    role: str
    industry: Optional[str] = None
    status: StatusEnum = StatusEnum.applied
    date_applied: date = date.today()
    notes: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[StatusEnum] = None
    date_applied: Optional[date] = None
    notes: Optional[str] = None


class ApplicationOut(ApplicationBase):
    id: int

    class Config:
        from_attributes = True
