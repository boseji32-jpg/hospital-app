export type UserRole = "admin" | "doctor" | "nurse" | "staff"

export interface User {
  email: string
  full_name: string
  role: UserRole
}

export interface LoginResponse {
  access_token: string
  token_type: string
  user: User
}

export interface Patient {
  id: number
  mrn: string
  first_name: string
  last_name: string
  date_of_birth: string
  gender: string
  phone: string
  email: string
  address: string
  patient_type: "inpatient" | "outpatient"
  admission_date: string | null
  discharge_date: string | null
  assigned_doctor_id: number | null
  created_at: string
  updated_at: string
}

export interface DashboardStats {
  total_patients: number
  inpatients: number
  outpatients: number
  doctors: number
  staff_count: number
}
