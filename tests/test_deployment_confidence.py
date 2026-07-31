from scripts.deployment_confidence import (
    calculate_score,
    recommendation,
)

def test_recommendation_deploy():
    assert recommendation(95) == "DEPLOY"

def test_recommendation_monitoring():
    assert recommendation(80) == "DEPLOY WITH MONITORING"

def test_recommendation_review():
    assert recommendation(65) == "REVIEW BEFORE DEPLOYMENT"

def test_recommendation_reject():
    assert recommendation(40) == "DO NOT DEPLOY"


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