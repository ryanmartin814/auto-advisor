from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# The OpenAI client will use OPENAI_API_KEY from the environment if available.
# This avoids hardcoding secrets in source code.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_explanation(loan_details: dict, loan_score: float) -> str:
    """
    loan_details: dict with all inputs and calculated fields
    loan_score: numeric 0-100
    """
    prompt = f"""
You are a financial AI advisor. Analyze the following car loan offer in detail:

User details:
- Age: {loan_details['age']}
- Monthly income: ${loan_details['monthly_income']}
- Credit score: {loan_details['credit_score']}

Loan details:
- Car: {loan_details['car_year']} {loan_details['car_make']} {loan_details['car_model']} {loan_details['car_trim']}
- Price: ${loan_details['car_price']}
- Down payment: ${loan_details['down_payment']}
- Loan term: {loan_details['term_months']} months
- APR: {loan_details['apr']}%
- Monthly payment: ${loan_details['monthly_payment']}
- Total interest: ${loan_details['total_interest']}
- Loan Score: {loan_score}

Please analyze the risk of the loan, including:
- Affordability relative to income
- Impact of credit score
- How the car affects risk (depreciation, make/model/trim reliability)
- APR and loan term considerations
- Anything else that may make the deal better or worse
- Compliment the user on any positive aspects of their situation (e.g. good credit score, large down payment, etc.)
- Provide a clear recommendation on whether this loan seems like a good deal or if they should consider other options.
- Compliment the car they are purchasing in a way someone who is excited and knowledgeable about their new car would appreciate.

Provide a clear, human-readable explanation, as if you were advising the user.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()