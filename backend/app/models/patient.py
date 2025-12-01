from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mrn: str = Field(index=True, unique=True)  # Medical Record Number
    first_name: str
    last_name: str
    date_of_birth: str  # YYYY-MM-DD
    gender: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None
    patient_type: str = Field(default="outpatient")  # inpatient / outpatient
    admission_date: Optional[str] = None
    discharge_date: Optional[str] = None
    assigned_doctor_id: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
