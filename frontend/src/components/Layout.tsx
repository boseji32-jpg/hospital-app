import { Outlet, Link, useNavigate } from "react-router-dom"
import { useAuth } from "../context/AuthContext"
import { LogOut, Users, LayoutDashboard, Hospital } from "lucide-react"

export default function Layout() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate("/login")
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navbar */}
      <nav className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center space-x-8">
              <Link to="/" className="flex items-center space-x-3">
                <Hospital className="w-8 h-8 text-blue-600" />
                <span className="text-xl font-semibold">Hospital Portal</span>
              </Link>
              <div className="hidden sm:flex space-x-6">
                <Link to="/" className="text-gray-700 hover:text-blue-600 flex items-center space-x-2">
                  <LayoutDashboard className="w-5 h-5" />
                  <span>Dashboard</span>
                </Link>
                <Link to="/patients" className="text-gray-700 hover:text-blue-600 flex items-center space-x-2">
                  <Users className="w-5 h-5" />
                  <span>Patients</span>
                </Link>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-600">
                {user?.full_name} ({user?.role})
              </span>
              <button
                onClick={handleLogout}
                className="text-gray-600 hover:text-red-600 flex items-center space-x-2"
              >
                <LogOut className="w-5 h-5" />
                <span className="hidden sm:inline">Logout</span>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Outlet />
      </main>
    </div>
  )
}
