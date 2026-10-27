"""Passing tests that also prove the dependency install stage worked."""

from __future__ import annotations

import pytest
import six

from calculator import add, divide, multiply, subtract


def test_addition() -> None:
    assert add(2, 3) == 5


def test_subtraction() -> None:
    assert subtract(10, 4) == 6


def test_multiplication() -> None:
    assert multiply(6, 7) == 42


def test_division() -> None:
    assert divide(9, 3) == 3


def test_division_by_zero_raises() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_installed_dependency_is_importable() -> None:
    """Fails if requirements.txt was not installed inside the container."""
    assert six.__version__ == "1.16.0"
