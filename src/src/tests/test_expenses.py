from src.expenses import add_expense, total_expenses
import pytest

def test_add_expense():
    expense = add_expense(10, "food", "lunch")
    assert expense["value"] == 10

def test_negative_value():
    with pytest.raises(ValueError):
        add_expense(-5, "food", "error")

def test_total():
    add_expense(20, "test", "test")
    total = total_expenses()
    assert total >= 20
