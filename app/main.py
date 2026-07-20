from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import projects
from app.routers import auth
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Cloud Deployment API",
    description="A FastAPI application for managing cloud deployment projects.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.include_router(auth_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(projects.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {
        "message": "CI/CD Pipeline API is running"
    }