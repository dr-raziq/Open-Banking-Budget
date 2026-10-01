import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.budget import calculate_budget_summary
from app.mock_data import MOCK_TRANSACTIONS

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == len(MOCK_TRANSACTIONS)
    assert data[0]["currency"] == "EUR"

def test_get_budget_summary():
    response = client.get("/budget/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_income" in data
    assert "total_expenses" in data
    assert "net_balance" in data
    assert isinstance(data["category_breakdown"], list)

def test_budget_calculation_income():
    summary = calculate_budget_summary(MOCK_TRANSACTIONS)
    assert summary.total_income == 2500.00

def test_budget_calculation_expenses():
    summary = calculate_budget_summary(MOCK_TRANSACTIONS)
    expected = sum(abs(t.amount) for t in MOCK_TRANSACTIONS if t.amount < 0)
    assert summary.total_expenses == round(expected, 2)

def test_budget_net_balance():
    summary = calculate_budget_summary(MOCK_TRANSACTIONS)
    assert summary.net_balance == round(summary.total_income - summary.total_expenses, 2)

def test_budget_category_breakdown():
    summary = calculate_budget_summary(MOCK_TRANSACTIONS)
    categories = [item.category for item in summary.category_breakdown]
    assert "Groceries" in categories
    assert "Transport" in categories