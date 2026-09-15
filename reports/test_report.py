from report_generator import generate_report
customer_id = "C001"
income = 80000
spending_score = 85
persona = "High-Value Customer"
reason = (
    "The customer has a high income and a high "
    "spending score, indicating strong purchasing capacity."
)
recommendations = [
    "Premium products",
    "Exclusive loyalty rewards",
    "Early access to new products",
    "Personalized premium offers"
]
file = generate_report(
    customer_id,
    income,
    spending_score,
    persona,
    reason,
    recommendations
)
print("Report generated successfully.")
print("File:", file)