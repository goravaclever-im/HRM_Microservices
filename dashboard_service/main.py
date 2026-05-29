from fastapi import FastAPI

app = FastAPI()


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Dashboard Service Running"
    }


# -----------------------------------
# DASHBOARD STATS
# -----------------------------------

@app.get("/dashboard/stats")
def dashboard_stats():

    return {

        "totalEmployees": 120,

        "activeEmployees": 110,

        "departments": 8,

        "pendingLeaves": 6,

        "todayAttendance": 95,

        "attendanceRate": 86
    }


# -----------------------------------
# RECENT EMPLOYEES
# -----------------------------------

@app.get("/dashboard/recent-employees")
def recent_employees():

    employees = [

        {
            "id": 1,
            "name": "Mahesh",
            "department": "HR"
        },

        {
            "id": 2,
            "name": "Rahul",
            "department": "IT"
        },

        {
            "id": 3,
            "name": "Sneha",
            "department": "Finance"
        },

        {
            "id": 4,
            "name": "Arjun",
            "department": "Operations"
        },

        {
            "id": 5,
            "name": "Priya",
            "department": "Recruitment"
        }
    ]

    return employees


# -----------------------------------
# DEPARTMENT STATS
# -----------------------------------

@app.get("/dashboard/department-stats")
def department_stats():

    result = [

        {
            "name": "HR",
            "count": 12
        },

        {
            "name": "IT",
            "count": 35
        },

        {
            "name": "Finance",
            "count": 15
        },

        {
            "name": "Operations",
            "count": 28
        }
    ]

    return result