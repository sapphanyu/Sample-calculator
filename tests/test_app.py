import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import json
from app import app, save_history

# --------------------------
# Fixtures
# --------------------------
@pytest.fixture
def client():
    """Create a Flask test client"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_history_before_tests():
    """Clear calculation history before each test to isolate tests"""
    save_history([])

# --------------------------
# Web page tests
# --------------------------
def test_home_page(client):
    """Test that the calculator home page loads correctly"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculator" in response.data

def test_history_page_empty(client):
    """Test that history page shows message when history is empty"""
    response = client.get("/h")
    assert response.status_code == 200
    assert b"No calculation history yet" in response.data

# --------------------------
# API tests for normal calculations (valid only)
# --------------------------
@pytest.mark.parametrize(
    "num1,num2,operator,expected",
    [
        (2, 3, "+", 5),
        (10, 5, "-", 5),
        (4, 2, "*", 8),
        (9, 3, "/", 3),
        (2, 3, "**", 8)
    ],
    ids=[
        "API add 2 + 3",
        "API subtract 10 - 5",
        "API multiply 4 * 2",
        "API divide 9 / 3",
        "API power 2 ** 3"
    ]
)
def test_calculate_api(client, num1, num2, operator, expected):
    """Test /CalculateTest API endpoint for valid calculations"""
    payload = {"num1": num1, "num2": num2, "operator": operator}
    response = client.post("/CalculateTest", json=payload)
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == expected

# --------------------------
# API test for invalid operator
# --------------------------
def test_calculate_invalid_operator(client):
    """Test /CalculateTest API endpoint with an invalid operator"""
    payload = {"num1": 2, "num2": 2, "operator": "%"}
    response = client.post("/CalculateTest", json=payload)
    assert response.status_code == 400
    assert "error" in response.get_json()

# --------------------------
# API tests for edge cases
# --------------------------
@pytest.mark.parametrize(
    "num1,num2,operator,expected",
    [
        (5, 0, "/", None),   # divide by zero
        (0, 0, "/", None),   # 0 / 0
        (5, 0, "**", 1),     # any number ** 0
        (0, 5, "**", 0),     # 0 ** positive
        (0, 0, "**", 1)      # 0 ** 0
    ],
    ids=[
        "API divide 5 / 0",
        "API divide 0 / 0",
        "API power 5 ** 0",
        "API power 0 ** 5",
        "API power 0 ** 0"
    ]
)
def test_calculate_api_edge_cases(client, num1, num2, operator, expected):
    """Test /CalculateTest API endpoint for divide-by-zero and power-by-zero edge cases"""
    payload = {"num1": num1, "num2": num2, "operator": operator}
    response = client.post("/CalculateTest", json=payload)
    data = response.get_json()

    if operator == "/" and num2 == 0:
        # Division by zero should return HTTP 400
        assert response.status_code == 400
        assert "error" in data
    else:
        # Power cases or valid calculations
        assert response.status_code == 200
        assert data["result"] == expected

# --------------------------
# Test history workflow
# --------------------------
def test_history_flow(client):
    """Test full history workflow: add, retrieve, and clear history"""
    # Add a calculation
    client.post("/CalculateTest", json={"num1": 1, "num2": 2, "operator": "+"})

    # Check history contains it
    response = client.get("/historyTest")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["result"] == 3

    # Clear history
    response = client.delete("/historyTest")
    data = response.get_json()
    assert data["message"] == "History cleared."

    # History should now be empty
    response = client.get("/historyTest")
    assert response.get_json() == []
