from sqlmodel import Session, select
from app.database import engine
from app.models.user import User
from app.models.patient import Patient
from passlib.context import CryptContext
from datetime import datetime
import random

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Staff users (email:password pairs – remember these!)
staff_data = [
    {"email": "admin@hospital.com",    "password": "admin123",  "full_name": "Dr. Admin",      "role": "admin"},
    {"email": "dr.raj@hospital.com",  "password": "doctor123", "full_name": "Dr. Raj Kumar",  "role": "doctor"},
    {"email": "dr.ani@hospital.com",  "password": "doctor123", "full_name": "Dr. Anitha",     "role": "doctor"},
    {"email": "nurse1@hospital.com",  "password": "nurse123",  "full_name": "Nurse Priya",    "role": "nurse"},
    {"email": "nurse2@hospital.com",  "password": "nurse123",  "full_name": "Nurse Lakshmi",  "role": "nurse"},
    {"email": "staff1@hospital.com",  "password": "staff123",  "full_name": "Staff Arun",     "role": "staff"},
    {"email": "staff2@hospital.com",  "password": "staff123",  "full_name": "Staff Vijay",    "role": "staff"},
    {"email": "staff3@hospital.com",  "password": "staff123",  "full_name": "Staff Meena",    "role": "staff"},
    {"email": "staff4@hospital.com",  "password": "staff123",  "full_name": "Staff Kumar",    "role": "staff"},
    {"email": "staff5@hospital.com",  "password": "staff123",  "full_name": "Staff Sonia",    "role": "staff"},
]

patient_names = [
    ("Aarav", "Sharma"), ("Isha", "Patel"), ("Vihaan", "Singh"), ("Diya", "Gupta"),
    ("Arjun", "Reddy"), ("Ananya", "Mehta"), ("Reyansh", "Jain"), ("Saanvi", "Verma"),
    ("Ayaan", "Nair"), ("Pari", "Yadav"), ("Kabir", "Malhotra"), ("Myra", "Shah"),
    ("Aryan", "Joshi"), ("Avani", "Rao"), ("Rudra", "Bose"), ("Sia", "Chopra"),
    ("Krish", "Desai"), ("Riya", "Menon"), ("Shaurya", "Iyer"), ("Aditi", "Banerjee")
]

genders = ["Male", "Female", "Other"]
patient_types = ["inpatient", "outpatient"]

with Session(engine) as session:
    # Seed staff users (only if not exist)
    for staff in staff_data:
        if not session.exec(select(User).where(User.email == staff["email"])).first():
            user = User(
                email=staff["email"],
                hashed_password=get_password_hash(staff["password"]),
                full_name=staff["full_name"],
                role=staff["role"]
            )
            session.add(user)
    
    session.commit()

    # Seed 20 patients
    for i in range(20):
        first, last = patient_names[i]
        mrn = f"MRN{2025000 + i:04d}"
        patient_type = random.choice(patient_types)
        admission = None
        discharge = None
        doctor_id = None
        
        if patient_type == "inpatient":
            admission = "2025-11-01"
            if random.random() > 0.4:
                discharge = "2025-11-15"
            doctor_id = random.choice([1, 2, 3])  # admin, dr.raj, dr.ani
        
        patient = Patient(
            mrn=mrn,
            first_name=first,
            last_name=last,
            date_of_birth=f"{random.randint(1950, 2005)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            gender=random.choice(genders),
            phone=f"+91{random.randint(7000000000, 9999999999)}",
            email=f"{first.lower()}.{last.lower()}@example.com",
            address=f"{i+1}, Random Street, Chennai, Tamil Nadu",
            patient_type=patient_type,
            admission_date=admission,
            discharge_date=discharge,
            assigned_doctor_id=doctor_id
        )
        session.add(patient)
    
    session.commit()
    print("Successfully seeded 10 staff users and 20 patients!")
    print("\nLogin credentials to remember:")
    print("Admin   → admin@hospital.com    / admin123")
    print("Doctor  → dr.raj@hospital.com   / doctor123")
    print("Nurse   → nurse1@hospital.com   / nurse123")
    print("Staff   → staff1@hospital.com   / staff123")
