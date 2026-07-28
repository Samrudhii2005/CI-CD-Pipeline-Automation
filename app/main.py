from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import projects
from app.routers import auth

from app.routers import projects, auth, dashboard
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Cloud Deployment API",
    description="A FastAPI application for managing cloud deployment projects.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")



@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(projects.router)
app.include_router(auth.router)
app.include_router(dashboard.router)

from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/dashboard")

@app.get("/healthzz")
def health_check():
    return {
        "status": "healthy"
    }