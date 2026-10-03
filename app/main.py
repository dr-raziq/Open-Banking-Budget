from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import List

from app.models import Transaction, BudgetSummary
from app.mock_data import MOCK_TRANSACTIONS
from app.budget import calculate_budget_summary


app = FastAPI(
    title="Open Banking Budget API",
    description="A mock open banking transaction and budgeting API for the European market.",
    version="1.0.0"
)


AVAILABLE_ENDPOINTS = [
    "/",
    "/transactions",
    "/budget/summary",
    "/health",
    "/docs",
    "/redoc",
    "/openapi.json"
]


@app.get("/")
def root():
    return {
        "name": "Open Banking Budget API",
        "version": "1.0.0",
        "description": "Mock open banking transaction and budgeting API for the European market.",
        "endpoints": AVAILABLE_ENDPOINTS
    }


@app.get("/transactions", response_model=List[Transaction])
def get_transactions():
    return MOCK_TRANSACTIONS


@app.get("/budget/summary", response_model=BudgetSummary)
def get_budget_summary():
    return calculate_budget_summary(MOCK_TRANSACTIONS)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "path": str(request.url.path),
            "available_endpoints": AVAILABLE_ENDPOINTS
        }
    )