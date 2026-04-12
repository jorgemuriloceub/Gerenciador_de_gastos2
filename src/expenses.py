import json
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(value, category, description):
    if value <= 0:
        raise ValueError("Valor deve ser positivo")

    expenses = load_expenses()

    expense = {
        "id": len(expenses) + 1,
        "value": value,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)
    return expense

def list_expenses():
    return load_expenses()

def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [e for e in expenses if e["id"] != expense_id]
    save_expenses(expenses)

def total_expenses():
    expenses = load_expenses()
    return sum(e["value"] for e in expenses)
