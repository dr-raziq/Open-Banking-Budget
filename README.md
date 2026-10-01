Open Banking Budget API



Overview
    The Open Banking Budget API is a Python FastAPI application that demonstrates how transaction data from European open banking providers can be aggregated into a simple budgeting summary. The application uses mock transaction data, so it runs without external API credentials. It includes tests, documentation, and deployment configuration for Render and Vercel.
    The project is structured as a reference implementation for PSD2-aligned Account Information Services (AIS) in the European market. It does not process real bank data and does not implement payment initiation.



What This Project Is About
    Open banking under PSD2 requires third-party providers to obtain authorisation and qualified certificates before accessing bank APIs directly. Most independent developers use a licensed aggregator instead. This project models the aggregator pattern: the application receives standardised transaction data and turns it into a user-facing budgeting view.
    The mock data approach means the project can be demonstrated, tested, and reviewed without signing up for a provider account or handling real financial data. It is suitable for learning, prototyping, and teaching the data layer that sits behind an open banking integration.



The API exposes two main endpoints:
    •	`GET /transactions` returns a list of mock transactions with fields that mirror the Account Information API response structure used by European open banking aggregators.
    •	`GET /budget/summary` returns a budget summary calculated from the same mock data, including total income, total expenses, net balance, and a breakdown by spending category.

    The mock data covers multiple categories such as groceries, transport, utilities, and subscriptions. The budget logic groups transactions by category and calculates totals.



How It Works
    1. Mock transactions are defined in `app/mock_data.py` using a Pydantic model that follows common open banking field naming conventions.
    2. The budget calculation logic in `app/budget.py` iterates over the transactions, separates income from expenses, and aggregates totals by category.
    3. FastAPI routes in `app/main.py` expose the transaction list and the calculated summary as JSON.
    4. Tests in `tests/test_app.py` verify the endpoints and the budget calculation using the mock data.

    The application is stateless and does not require a database. All data is held in memory for the lifetime of the process.



Use Cases
    •	Learning how PSD2 account information data can be modelled and transformed.
    •	Prototyping a budgeting or personal finance feature without connecting to a real bank.
    •	Testing API design and data validation with FastAPI and Pydantic.
    •	Demonstrating a deployable Python service on free hosting tiers.
    •	Serving as a starting point for integrating a real open banking aggregator such as GoCardless, TrueLayer, or Yapily.



Stack

    Component 	-> Technology 

    Language -> Python 3.11 
    Web Framework -> FastAPI 
    Data Validation -> Pydantic 
    ASGI Server -> Uvicorn 
    Testing -> Pytest 
    Deployment -> Render or Vercel 



Project Structure
    Open Banking Budget 
    |_ app
    |	|_ __init__.py
    |	|_ main.py
    |	|_ models.py
    |	|_ mock_data.py
    |	|_  budget.py
    |
    |_ tests
    |	|_ test_app.py
    |
    |_ requirements.txt
    |_ Procfile
    |_ render.yaml
    |_ vercel.json
    |_ README.md



Path & Description 
    I.	`app/main.py` -> FastAPI application and route definitions 
    II.	`app/models.py` -> Pydantic models for transactions and budget summary 
    III.	`app/mock_data.py` -> Mock transaction dataset 
    IV.	`app/budget.py` -> Budget calculation logic 
    V.	`tests/test_app.py` -> Endpoint and calculation tests 
    VI.	`requirements.txt` -> Python dependencies 
    VII.	`Procfile` -> Process definition for Render 
    VIII.	`render.yaml` -> Render deployment configuration 
    IX.	`vercel.json` -> Vercel deployment configuration 



How to Run Locally
    1.	Clone the repository and create a virtual environment:
    2.	git clone https://github.com/<your-username>/open-banking-budget.git
    3.	cd open-banking-budget
    4.	python -m venv .venv
    5.	source .venv/bin/activate

Install dependencies:
    pip install -r requirements.txt

Start the API:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

    The API is available at `http://0.0.0.0:8000/transactions`. Interactive documentation is available at `http://0.0.0.0:8000/docs`.

How to Run Tests
    python -m pytest tests/ -v

    The tests cover the transaction endpoint, the budget summary endpoint, and the budget calculation logic. All tests use the mock data, so no external services or credentials are required.



API Reference

    GET /transactions
        Returns a JSON array of transaction objects.
        Response example:
        [
        {
            "id": "txn-001",
            "date": "2026-09-01",
            "amount": -45.20,
            "currency": "EUR",
            "description": "Supermarket",
            "category": "Groceries",
            "merchant": "Tesco"
        }
        ]

    GET /budget/summary
        Returns a budget summary calculated from all transactions.
        Response example:
        {
        "total_income": 2500.00,
        "total_expenses": 1470.50,
        "net_balance": 1029.50,
        "currency": "EUR",
        "category_breakdown": [
            {"category": "Groceries", "total": 320.40, "count": 8},
            {"category": "Transport", "total": 95.00, "count": 4}
        ]
        }

    GET /health
        Returns a simple health check response.
        Response example:
        {"status": "ok"}



Data Model
    Each transaction follows the field naming conventions used by open banking aggregators where practical.

    Field -> Type -> Description 

    `id` -> string -> Unique transaction identifier 
    `date` -> string -> ISO 8601 date 
    `amount` -> float -> Negative for expenses, positive for income 
    `currency` -> string -> ISO 4217 currency code 
    `description` -> string -> Human-readable description 
    `category` -> string -> Spending category 
    `merchant` -> string -> Merchant name 

    The currency is set to EUR to reflect the European market context. The model can be extended to support multi-currency data.



PSD2 Context

    The European Second Payment Services Directive (PSD2) requires banks to provide licensed third parties with access to customer account data through standardised APIs. An Account Information Service Provider (AISP) can read balances and transactions with the customer's explicit consent.

    This project does not implement the consent redirect flow or call a bank's API directly. It models the data layer that sits behind an aggregator integration. A production implementation would add:
        I. OAuth 2.0 authorisation flow with an aggregator such as GoCardless (Nordigen), TrueLayer, or Yapily
        II. Token storage and refresh handling
        III. Consent expiry tracking
        IV. Error handling for bank API rate limits

    The mock data approach keeps the project focused on the budgeting domain logic and makes the application reviewable without regulatory setup.



Deployment

    Render

            1. Push the repository to GitHub.
            2. Create a new Web Service on Render.
            3. Connect the GitHub repository.
            4. Set the build command to `pip install -r requirements.txt`.
            5. Set the start command to `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
            6. Select the free instance type.

        Render provides a public URL after the first deploy. The free tier sleeps after inactivity and does not require a credit card.


    Vercel

        The project includes a `vercel.json` configuration for serverless deployment. Vercel supports Python ASGI applications through its Python runtime. After deploying, the API is available at the assigned Vercel URL.

        To deploy with the Vercel CLI:
            npm i -g vercel
            vercel --prod

        Vercel's free tier includes serverless function execution and automatic HTTPS.



Running with Real Sandbox Providers

    To extend the project to use a real open banking sandbox instead of the built-in mock data, the main change is replacing `app/mock_data.py` with a client that calls the provider's API. The budget logic in `app/budget.py` and the API layer in `app/main.py` remain the same because both expect the same transaction model.

    The three providers referenced in this project each offer free sandbox access.

        a.	GoCardless (formerly Nordigen)

            i.	GoCardless provides a free Bank Account Data API that covers over 2,300 European banks. The official Python client is available on PyPI as `nordigen`. Credentials are obtained from the GoCardless Bank Account Data Portal as a `SECRET_ID` and `SECRET_KEY`. The client is then used to list institutions, create a requisition, and fetch transactions.

        b.	TrueLayer

            i.	TrueLayer offers a free sandbox environment where integrations can be tested without live bank accounts. After creating a Console account, a sandbox `client_id` (prefixed with `sandbox-`) and a `client_secret` are issued. The sandbox uses mock bank data and does not move real money.

        c.	Yapily

            i.	Yapily provides a sandbox environment with a preconfigured Modelo Sandbox. An application is registered at the Yapily dashboard to obtain credentials. The Python SDK is then used to retrieve institutions, accounts, and transactions.

            ii.	In all three cases, a production integration would require handling OAuth redirects, consent management, and token refresh. Those flows are outside the scope of this project, which focuses on the data transformation and budgeting layer that sits behind the aggregator.