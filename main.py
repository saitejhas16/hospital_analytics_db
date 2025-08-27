from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from typing import List, Dict

app = FastAPI()

# -----------------------------
# CORS Settings
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Open for testing, later you can restrict to your GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Database Configuration
# -----------------------------
DB_USER = "saitejhas"                     # AlwaysData MySQL username
DB_PASS = "Saitejhas1610*"                # AlwaysData MySQL password
DB_HOST = "mysql-saitejhas.alwaysdata.net"  # Host from AlwaysData
DB_NAME = "saitejhas_hospital_db"         # Your database name

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# -----------------------------
# Helper Function to Fetch Table Data
# -----------------------------
def fetch_table(table_name: str) -> List[Dict]:
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        # 🔹 Convert rows to dicts properly
        data = [dict(row._mapping) for row in result]
    return data


# -----------------------------
# API Endpoints
# -----------------------------
@app.get("/")
def root():
    return {"message": "Hospital API is running"}

@app.get("/departments")
def get_departments():
    return fetch_table("departments")

@app.get("/patients")
def get_patients():
    return fetch_table("patients")

@app.get("/staff")
def get_staff():
    return fetch_table("staff")

@app.get("/beds")
def get_beds():
    return fetch_table("beds")

@app.get("/admissions")
def get_admissions():
    return fetch_table("admissions")

@app.get("/resource_utilization")
def get_resource_utilization():
    return fetch_table("resource_utilization")

@app.get("/equipment")
def get_equipment():
    return fetch_table("equipment")

@app.get("/disease_symptoms")
def get_equipment():
    return fetch_table("disease_symptoms")