from typing import List, Dict
from app.models import Transaction, BudgetSummary, CategoryBreakdown

def calculate_budget_summary(transactions: List[Transaction]) -> BudgetSummary:
    total_income = 0.0
    total_expenses = 0.0
    category_totals: Dict[str, Dict[str, float]] = {}

    for txn in transactions:
        if txn.amount > 0:
            total_income += txn.amount
        else:
            total_expenses += abs(txn.amount)

        if txn.category not in category_totals:
            category_totals[txn.category] = {"total": 0.0, "count": 0}

        category_totals[txn.category]["total"] += abs(txn.amount)
        category_totals[txn.category]["count"] += 1

    breakdown = [
        CategoryBreakdown(
            category=cat,
            total=round(data["total"], 2),
            count=int(data["count"])
        )
        for cat, data in sorted(category_totals.items(), key=lambda x: x[1]["total"], reverse=True)
    ]

    return BudgetSummary(
        total_income=round(total_income, 2),
        total_expenses=round(total_expenses, 2),
        net_balance=round(total_income - total_expenses, 2),
        category_breakdown=breakdown
    )