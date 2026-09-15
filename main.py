from analytics.history import (
    save_prediction,
    get_prediction_history
)
customer_id = "C001"
income = 80000
spending_score = 85
persona = "High-Value Customer"
save_prediction(
    customer_id,
    income,
    spending_score,
    persona
)
print("Prediction saved successfully.")
history = get_prediction_history()
print("\nPREDICTION HISTORY")
print("=" * 60)
print(history)