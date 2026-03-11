from fastapi import FastAPI
from pydantic import BaseModel

from app.loan_calculator import monthly_payment, total_interest

app = FastAPI()

class LoanInput(BaseModel):
    car_price: float
    down_payment: float
    apr: float
    term_months: int
    monthly_income: float
    credit_score: int
    age: int

@app.get("/")
def home():
    return {"message": "Car Load AI Advisor API"}

@app.post("/analyze-loan")
def analyze_loan(data: LoanInput):
    principal = data.car_price - data.down_payment
    payment = monthly_payment(principal, data.apr, data.term_months)
    interest = total_interest(payment, data.term_months, principal)

    return {
        "loan_amount": principal,
        "monthly_payment": payment,
        "total_interest": interest
    }