import sys
import os

# Add src folder to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
import main

# --- Unit tests for basic math operations ---

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-1, 5, 4),
        (0, 0, 0)
    ],
    ids=[
        "adding 2 + 3",
        "adding -1 + 5",
        "adding 0 + 0"
    ]
)
def test_add_numbers(a, b, expected):
    """Test addition of two numbers"""
    assert main.add_numbers(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 5, -5)
    ],
    ids=[
        "subtracting 5 - 3",
        "subtracting 0 - 5"
    ]
)
def test_subtract_numbers(a, b, expected):
    """Test subtraction of two numbers"""
    assert main.subtract_numbers(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-1, 5, -5)
    ],
    ids=[
        "multiplying 2 * 3",
        "multiplying -1 * 5"
    ]
)
def test_multiply_numbers(a, b, expected):
    """Test multiplication of two numbers"""
    assert main.multiply_numbers(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (5, 2, 2.5)
    ],
    ids=[
        "dividing 6 / 3",
        "dividing 5 / 2"
    ]
)
def test_divide_numbers(a, b, expected):
    """Test division of two numbers (normal cases)"""
    assert main.divide_numbers(a, b) == expected


def test_divide_by_zero():
    """Test that dividing by zero returns None"""
    assert main.divide_numbers(5, 0) is None
    assert main.divide_numbers(0, 0) is None  # also edge case: 0 / 0


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 8),
        (5, 0, 1),  # any number ** 0 = 1
        (0, 5, 0),  # 0 ** any positive = 0
        (0, 0, 1)   # 0 ** 0 is conventionally 1 in Python
    ],
    ids=[
        "power 2 ** 3",
        "power 5 ** 0",
        "power 0 ** 5",
        "power 0 ** 0"
    ]
)
def test_power_numbers(a, b, expected):
    """Test exponentiation (power) including edge cases with 0"""
    assert main.power_numbers(a, b) == expected


# --- Test parsing function ---
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("1 + 2", (1.0, 2.0, "+")),
        ("3.5 * 2", (3.5, 2.0, "*"))
    ],
    ids=[
        "parsing '1 + 2'",
        "parsing '3.5 * 2'"
    ]
)
def test_get_numbers_and_operator_butnoprint_valid(input_str, expected):
    """Test parsing valid input strings returns correct numbers and operator"""
    assert main.get_numbers_and_operator_butnoprint(input_str) == expected


@pytest.mark.parametrize(
    "input_str,error_msg",
    [
        ("1 $ 2", "Invalid operator"),
        ("a + b", "Invalid number input"),
        ("1 +", "Invalid format")
    ],
    ids=[
        "invalid operator '1 $ 2'",
        "non-numeric input 'a + b'",
        "wrong format '1 +'"
    ]
)
def test_get_numbers_and_operator_butnoprint_invalid(input_str, error_msg):
    """Test parsing invalid input strings returns proper error message"""
    result = main.get_numbers_and_operator_butnoprint(input_str)
    assert error_msg in result
