from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, func
from typing import List
from app.models.patient import Patient
from app.models.user import User
from app.database import get_session
from app.utils.security import get_current_user

router = APIRouter(prefix="/api/patients", tags=["Patients"])

@router.get("/", response_model=List[Patient])
def list_patients(
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    patients = session.exec(select(Patient).offset(skip).limit(limit)).all()
    return patients

@router.get("/dashboard")
def dashboard(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    total = session.exec(select(func.count()).select_from(Patient)).one()
    inpatients = session.exec(select(func.count()).select_from(Patient).where(Patient.patient_type == "inpatient")).one()
    outpatients = session.exec(select(func.count()).select_from(Patient).where(Patient.patient_type == "outpatient")).one()
    doctors = session.exec(select(func.count()).select_from(User).where(User.role == "doctor")).one()
    
    return {
        "total_patients": total,
        "inpatients": inpatients,
        "outpatients": outpatients,
        "doctors": doctors,
        "staff_count": 10
    }
