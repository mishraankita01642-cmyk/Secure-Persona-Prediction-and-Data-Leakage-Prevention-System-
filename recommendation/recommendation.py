def get_recommendations(persona):
    recommendations = {
        "High-Value Customer": [
            "Premium products",
            "Exclusive loyalty rewards",
            "Early access to new products",
            "Personalized premium offers"
        ],
        "Budget Customer": [
            "Budget-friendly products",
            "Discount coupons",
            "Combo offers",
            "Seasonal sale products"
        ],
        "Potential Customer": [
            "Premium trial offers",
            "Personalized promotions",
            "First-purchase discounts",
            "Product demonstrations"
        ],
        "Impulsive Spender": [
            "Limited-time offers",
            "Flash sales",
            "Trending products",
            "Personalized deals"
        ]
    }
    return recommendations.get(
        persona,
        ["General product recommendations"]
    )
def get_explanation(persona, income, spending_score):
    if persona == "High-Value Customer":
        return (
            f"The customer has an income of Rs.{income} "
            f"and a spending score of {spending_score}. "
            "High income and high spending behaviour indicate "
            "strong purchasing capacity."
        )
    elif persona == "Budget Customer":
        return (
            f"The customer has an income of Rs.{income} "
            f"and a spending score of {spending_score}. "
            "Lower income and spending behaviour indicate "
            "price-sensitive purchasing behaviour."
        )
    elif persona == "Potential Customer":
        return (
            f"The customer has an income of Rs.{income} "
            f"and a spending score of {spending_score}. "
            "The customer has good purchasing capacity but "
            "comparatively lower spending behaviour."
        )
    elif persona == "Impulsive Spender":
        return (
            f"The customer has an income of Rs.{income} "
            f"and a spending score of {spending_score}. "
            "High spending relative to income indicates "
            "strong spending behaviour."
        )
    return "General customer segment."