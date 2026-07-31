def calculate_deployment_confidence(
    tests_passed: bool,
    coverage: float,
    quality_gate_passed: bool,
    health_check_passed: bool
):
    # Test Score
    test_score = 100 if tests_passed else 0

    # Coverage Score
    coverage_score = coverage

    # SonarQube Score
    sonar_score = 100 if quality_gate_passed else 0

    # Health Check Score
    health_score = 100 if health_check_passed else 0

    # Final Deployment Confidence Score
    score = (
        (0.35 * test_score) +
        (0.25 * coverage_score) +
        (0.20 * sonar_score) +
        (0.20 * health_score)
    )

    if score >= 90:
        recommendation = "Deploy"
    elif score >= 75:
        recommendation = "Deploy with Monitoring"
    elif score >= 60:
        recommendation = "Manual Review Required"
    else:
        recommendation = "Reject Deployment"

    return {
        "deployment_confidence_score": round(score, 2),
        "recommendation": recommendation
    }