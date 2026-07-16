from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "message": "Cloud Deployment Management System is running successfully."
    }