"""
predict persona
It loads the pre-trained model + scaler
(from train_model.py) and exposes one clean function:

    predict_cluster(age, gender, income, spending_score) -> int

"""

import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "kmeans_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Load once at import time (not on every call)
with open(MODEL_PATH, "rb") as f:
    _kmeans_model = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    _scaler = pickle.load(f)


def predict_cluster(age: int, gender: str, income: float, spending_score: float) -> int:
    """
    Takes a new user's details and returns their predicted cluster number.

    Parameters:
        age (int): user's age
        gender (str): "Male" or "Female"
        income (float): annual income (same units/scale as training data, e.g. k$)
        spending_score (float): spending score, typically 1-100

    Returns:
        int: cluster number (e.g. 0-4 if trained with k=5)
    """
    gender_encoded = 0 if gender.lower() == "male" else 1

    input_data = np.array([[age, gender_encoded, income, spending_score]])
    scaled_input = _scaler.transform(input_data)

    cluster = _kmeans_model.predict(scaled_input)[0]
    return int(cluster)


# Quick manual test — only runs if you execute this file directly
if __name__ == "__main__":
    test_cluster = predict_cluster(25, "Female", 60, 75)
    print(f"Predicted cluster: {test_cluster}")