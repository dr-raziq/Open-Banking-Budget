from app.models import Transaction

MOCK_TRANSACTIONS = [
    Transaction(id="txn-001", date="2026-09-01", amount=-45.20, description="Weekly grocery shopping", category="Groceries", merchant="Tesco"),
    Transaction(id="txn-002", date="2026-09-01", amount=-12.50, description="Bus fare", category="Transport", merchant="Dublin Bus"),
    Transaction(id="txn-003", date="2026-09-02", amount=-1200.00, description="Monthly rent", category="Housing", merchant="Landlord"),
    Transaction(id="txn-004", date="2026-09-02", amount=2500.00, description="Monthly salary", category="Income", merchant="Employer"),
    Transaction(id="txn-005", date="2026-09-03", amount=-67.30, description="Electricity bill", category="Utilities", merchant="Electric Ireland"),
    Transaction(id="txn-006", date="2026-09-04", amount=-9.99, description="Streaming subscription", category="Subscriptions", merchant="Netflix"),
    Transaction(id="txn-007", date="2026-09-05", amount=-38.60, description="Groceries", category="Groceries", merchant="Lidl"),
    Transaction(id="txn-008", date="2026-09-05", amount=-22.00, description="Dinner", category="Dining", merchant="Local Restaurant"),
    Transaction(id="txn-009", date="2026-09-06", amount=-55.00, description="Mobile phone bill", category="Utilities", merchant="Vodafone"),
    Transaction(id="txn-010", date="2026-09-07", amount=-15.75, description="Pharmacy", category="Health", merchant="Boots"),
    Transaction(id="txn-011", date="2026-09-08", amount=-89.00, description="Train ticket", category="Transport", merchant="Irish Rail"),
    Transaction(id="txn-012", date="2026-09-09", amount=-120.00, description="Clothing", category="Shopping", merchant="Penneys"),
    Transaction(id="txn-013", date="2026-09-10", amount=-32.40, description="Groceries", category="Groceries", merchant="Aldi"),
    Transaction(id="txn-014", date="2026-09-11", amount=-14.99, description="Music subscription", category="Subscriptions", merchant="Spotify"),
    Transaction(id="txn-015", date="2026-09-12", amount=-65.00, description="Dentist", category="Health", merchant="Dental Clinic"),
]