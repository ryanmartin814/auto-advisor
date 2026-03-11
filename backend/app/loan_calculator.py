def monthly_payment(principal, apr, months):
    monthly_rate = apr / 100 / 12
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    return round(payment, 2)

def total_interest(payment, months, principal):
    return round(payment * months - principal, 2)