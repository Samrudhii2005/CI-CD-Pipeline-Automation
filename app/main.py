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

# Create database tables automatically when the application starts
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(projects.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Cloud Deployment API",
        "documentation": "/docs",
        "redoc": "/redoc",
    }

@app.get("/")
def home():
    return {"message": "CI/CD Pipeline API is running"}