from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import projects

app = FastAPI(
    title="Cloud Deployment API",
    description="A FastAPI application for managing cloud deployment projects.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(projects.router)

@app.get("/")
def home():
    return {
        "message": "CI/CD Pipeline API is running"
    }