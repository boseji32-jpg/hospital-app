from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    full_name: str
    role: str = Field(default="staff")  # admin, doctor, nurse, staff
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
