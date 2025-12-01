import { useQuery } from "@tanstack/react-query"
import api from "../lib/api"
import { DashboardStats } from "../types"
import { Users, Bed, UserCheck, Activity } from "lucide-react"

export default function Dashboard() {
  const { data: stats, isLoading } = useQuery<DashboardStats>({
    queryKey: ["dashboard"],
    queryFn: () => api.get("/patients/dashboard").then(res => res.data),
  })

  const cards = [
    { title: "Total Patients", value: stats?.total_patients ?? 0, icon: Users, color: "blue" },
    { title: "Inpatients", value: stats?.inpatients ?? 0, icon: Bed, color: "green" },
    { title: "Outpatients", value: stats?.outpatients ?? 0, icon: Activity, color: "purple" },
    { title: "Doctors", value: stats?.doctors ?? 0, icon: UserCheck, color: "orange" },
  ]

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>
      
      {isLoading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="bg-white rounded-xl shadow-sm p-6 animate-pulse">
              <div className="h-4 bg-gray-200 rounded w-32 mb-4"></div>
              <div className="h-12 bg-gray-200 rounded w-20"></div>
            </div>
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {cards.map((card) => (
            <div key={card.title} className="bg-white rounded-xl shadow-sm p-6 hover:shadow-lg transition">
              <div className="flex items-center justify-between mb-4">
                <card.icon className={`w-10 h-10 text-${card.color}-600`} />
                <span className={`text-3xl font-bold text-${card.color}-600`}>{card.value}</span>
              </div>
              <h3 className="text-gray-600 text-sm">{card.title}</h3>
            </div>
          ))}
        </div>
      )}

      <div className="mt-12 bg-white rounded-xl shadow-sm p-8">
        <h2 className="text-2xl font-semibold mb-4">Welcome back!</h2>
        <p className="text-gray-600">Your hospital management system is up and running.</p>
      </div>
    </div>
  )
}
