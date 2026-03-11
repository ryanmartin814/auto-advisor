from fastapi import FastAPI
from pydantic import BaseModel

from app.loan_calculator import monthly_payment, total_interest
from app.loan_analyzer import analyze_risk
from app.loan_explainer import generate_explanation

app = FastAPI()

class LoanInput(BaseModel):
    car_price: float
    down_payment: float
    apr: float
    term_months: int
    monthly_income: float
    credit_score: int
    age: int
    car_year: int
    car_make: str
    car_model: str
    car_trim: str

@app.get("/")
def home():
    return {"message": "Car Load AI Advisor API"}

@app.post("/analyze-loan")
def analyze_loan(data: LoanInput):
    principal = data.car_price - data.down_payment
    payment = monthly_payment(principal, data.apr, data.term_months)
    interest = total_interest(payment, data.term_months, principal)
    score = analyze_risk(payment, data.monthly_income, data.credit_score, data.term_months, data.apr)

    loan_details = {
        "age": data.age,
        "monthly_income": data.monthly_income,
        "credit_score": data.credit_score,
        "car_year": data.car_year,
        "car_make": data.car_make,
        "car_model": data.car_model,
        "car_trim": data.car_trim,
        "car_price": data.car_price,
        "down_payment": data.down_payment,
        "term_months": data.term_months,
        "apr": data.apr,
        "monthly_payment": payment,
        "total_interest": interest
    }

    explanation = generate_explanation(loan_details, score)

    return {
        "loan_amount": principal,
        "monthly_payment": payment,
        "total_interest": interest,
        "loan_score": score,
        "explanation": explanation
    }