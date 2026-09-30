from fastapi import FastAPI
from typing import List
from app.models import Transaction, BudgetSummary
from app.mock_data import MOCK_TRANSACTIONS
from app.budget import calculate_budget_summary

app = FastAPI(
    title="Open Banking Budget API",
    description="A mock open banking transaction and budgeting API.",
    version="1.0.0"
)

@app.get("/transactions", response_model=List[Transaction])
def get_transactions():
    return MOCK_TRANSACTIONS

@app.get("/budget/summary", response_model=BudgetSummary)
def get_budget_summary():
    return calculate_budget_summary(MOCK_TRANSACTIONS)

@app.get("/health")
def health_check():
    return {"status": "ok"}