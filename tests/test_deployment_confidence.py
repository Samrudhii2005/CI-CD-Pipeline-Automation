from scripts.deployment_confidence import (
    calculate_score,
    recommendation,
)

from app.utils.deployment_confidence import calculate_deployment_confidence


# -------------------------------
# Deployment Confidence Tests
# -------------------------------

def test_deploy_recommendation():
    result = calculate_deployment_confidence(
        tests_passed=True,
        coverage=100,
        quality_gate_passed=True,
        health_check_passed=True
    )

    assert result["deployment_confidence_score"] == 100.0
    assert result["recommendation"] == "Deploy"


def test_deploy_with_monitoring():
    result = calculate_deployment_confidence(
        tests_passed=True,
        coverage=80,
        quality_gate_passed=True,
        health_check_passed=False
    )

    assert result["recommendation"] == "Deploy with Monitoring"


def test_manual_review():
    result = calculate_deployment_confidence(
        tests_passed=True,
        coverage=100,
        quality_gate_passed=False,
        health_check_passed=False
    )

    assert result["recommendation"] == "Manual Review Required"


def test_reject():
    result = calculate_deployment_confidence(
        tests_passed=False,
        coverage=20,
        quality_gate_passed=False,
        health_check_passed=False
    )

    assert result["recommendation"] == "Reject Deployment"


# -------------------------------
# Recommendation Function Tests
# -------------------------------

def test_recommendation_deploy():
    assert recommendation(95) == "DEPLOY"


def test_recommendation_monitoring():
    assert recommendation(80) == "DEPLOY WITH MONITORING"


def test_recommendation_review():
    assert recommendation(65) == "REVIEW BEFORE DEPLOYMENT"


def test_recommendation_reject():
    assert recommendation(40) == "DO NOT DEPLOY"


# -------------------------------
# Score Calculation Tests
# -------------------------------

def test_calculate_score_all_pass():
    score = calculate_score(
        tests=True,
        coverage=100,
        quality_gate=True,
        health=True
    )

    assert score == 100.0


def test_calculate_score_failed_tests():
    score = calculate_score(
        tests=False,
        coverage=80,
        quality_gate=True,
        health=True
    )

    assert score < 100


def test_calculate_score_without_quality_gate():
    score = calculate_score(
        tests=True,
        coverage=70,
        quality_gate=None,
        health=True
    )

    assert score > 0