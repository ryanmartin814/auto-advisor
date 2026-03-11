def analyze_risk(monthly_payment, monthly_income, credit_score, term_months, apr):
    score = 50  # base score

    dti = monthly_payment / monthly_income * 100
    if dti < 20:
        score += 20
    elif dti < 35:
        score += 10
    else:
        score -= 10

    if credit_score >= 750:
        score += 20
    elif credit_score >= 700:
        score += 15
    elif credit_score >= 650:
        score += 10
    else:
        score += 5

    if term_months <= 36:
        score += 10
    elif term_months <= 60:
        score += 5
    else:
        score -= 5

    if apr <= 6:
        score += 10
    elif apr <= 8:
        score += 5
    else:
        score -= 5

    score = max(0, min(100, score))
    return round(score, 1)