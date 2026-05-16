from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, HttpUrl


class ApplicationStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"


class ApplicationBase(BaseModel):
    fullName: str = Field(..., min_length=2, max_length=80, examples=["Ama Serwaa Owusu"])
    email: EmailStr = Field(..., examples=["amaserwaa@gmail.com"])
    phone: str = Field(..., min_length=10, max_length=15, pattern=r"^[0-9+]+$", examples=["0245567812"])
    whatsappNumber: str = Field(..., min_length=10, max_length=15, pattern=r"^[0-9+]+$", examples=["0245567812"])
    university: str = Field(..., min_length=2, max_length=100, examples=["KNUST"])
    course: str = Field(..., min_length=2, max_length=100, examples=["Computer Engineering"])
    level: str = Field(..., examples=["2nd Year"])
    track: str = Field(..., min_length=2, max_length=100, examples=["Backend Engineering"])
    motivation: str = Field(..., min_length=10, max_length=500)
    portfolioLink: Optional[HttpUrl] = None
    resumeLink: Optional[HttpUrl] = None
    joinInnovationClub: bool = False
    status: ApplicationStatus = ApplicationStatus.pending


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    fullName: Optional[str] = Field(None, min_length=2, max_length=80)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=10, max_length=15, pattern=r"^[0-9+]+$")
    whatsappNumber: Optional[str] = Field(None, min_length=10, max_length=15, pattern=r"^[0-9+]+$")
    university: Optional[str] = Field(None, min_length=2, max_length=100)
    course: Optional[str] = Field(None, min_length=2, max_length=100)
    level: Optional[str] = None
    track: Optional[str] = Field(None, min_length=2, max_length=100)
    motivation: Optional[str] = Field(None, min_length=10, max_length=500)
    portfolioLink: Optional[HttpUrl] = None
    resumeLink: Optional[HttpUrl] = None
    joinInnovationClub: Optional[bool] = None
    status: Optional[ApplicationStatus] = None


class ApplicationResponse(ApplicationBase):
    id: int
    submittedAt: str
