import xml.etree.ElementTree as ET
import requests
import os

TEST_WEIGHT = 0.35
COVERAGE_WEIGHT = 0.25
QUALITY_WEIGHT = 0.25
HEALTH_WEIGHT = 0.15

def get_coverage():
    tree = ET.parse("coverage.xml")
    root = tree.getroot()

    line_rate = float(root.attrib["line-rate"])

    return round(line_rate * 100, 2)


def get_health_status():
    try:
        response = requests.get("http://127.0.0.1:8000/health", timeout=5)
        return response.status_code == 200
    except Exception:
        return False

def get_test_status():
    return os.getenv("TESTS_PASSED", "false").lower() == "true"

def get_quality_gate():
    token = os.getenv("SONAR_TOKEN")

    if not token:
        return None

    url = (
        "https://sonarcloud.io/api/qualitygates/project_status"
        "?projectKey=Samrudhii2005_CI-CD-Pipeline-Automation"
    )

    try:
        response = requests.get(
            url,
            auth=(token, ""),
            timeout=10
        )

        if response.status_code != 200:
            return False

        data = response.json()

        return data["projectStatus"]["status"] == "OK"

    except Exception:
        return False

def calculate_score(tests, coverage, quality_gate, health):
    available_weight = 0
    score = 0

    if tests is not None:
        available_weight += TEST_WEIGHT
        if tests:
            score += TEST_WEIGHT * 100

    available_weight += COVERAGE_WEIGHT
    score += COVERAGE_WEIGHT * coverage

    if quality_gate is not None:
        available_weight += QUALITY_WEIGHT
        if quality_gate:
            score += QUALITY_WEIGHT * 100

    if health is not None:
        available_weight += HEALTH_WEIGHT
        if health:
            score += HEALTH_WEIGHT * 100

    if available_weight == 0:
        return 0

    return round(score / available_weight, 2)


def recommendation(score):


    if score >= 90:
        return "DEPLOY"

    elif score >= 75:
        return "DEPLOY WITH MONITORING"

    elif score >= 60:
        return "REVIEW BEFORE DEPLOYMENT"

    else:
        return "DO NOT DEPLOY"
    
if __name__ == "__main__":

    coverage = get_coverage()
    health = get_health_status()
    tests = get_test_status()
    quality_gate = get_quality_gate()

    score = calculate_score(
        tests,
        coverage,
        quality_gate,
        health
    )

    print("=" * 50)
    print("Pipeline Deployment Confidence Framework")
    print("=" * 50)

    print(f"Tests         : {'PASS' if tests else 'FAIL'}")
    print(f"Coverage      : {coverage}%")
    print(f"Health Check  : {'PASS' if health else 'FAIL'}")

    if quality_gate is None:
        print("Quality Gate  : SKIPPED (Local)")
    else:
        print(f"Quality Gate  : {'PASS' if quality_gate else 'FAIL'}")

    print("-" * 50)
    print(f"Deployment Confidence Score : {score}")
    print(f"Recommendation             : {recommendation(score)}")
    print("=" * 50)