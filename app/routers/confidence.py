from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.deployment_confidence import calculate_deployment_confidence

router = APIRouter(
    prefix="/confidence",
    tags=["Deployment Confidence Framework"]
)


class ConfidenceRequest(BaseModel):
    tests_passed: bool
    coverage: float
    quality_gate_passed: bool
    health_check_passed: bool


@router.post("/")
def calculate_score(request: ConfidenceRequest):
    return calculate_deployment_confidence(
        request.tests_passed,
        request.coverage,
        request.quality_gate_passed,
        request.health_check_passed
    )