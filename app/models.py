from pydantic import BaseModel, Field
from typing import List

class Transaction(BaseModel):
    id: str
    date: str
    amount: float
    currency: str = "EUR"
    description: str
    category: str
    merchant: str

class CategoryBreakdown(BaseModel):
    category: str
    total: float
    count: int

class BudgetSummary(BaseModel):
    total_income: float
    total_expenses: float
    net_balance: float
    currency: str = "EUR"
    category_breakdown: List[CategoryBreakdown]