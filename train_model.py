"""
train model
Trains a K-Means clustering model on customer data and saves it 
(along with the fitted scaler) so main.py can load it at runtime without retraining.

"""

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# 1. Load dataset
# Expecting a CSV with columns: Age, Gender, Annual_Income, Spending_Score
# Download "Mall_Customers.csv" (Kaggle) or use your own and rename columns
DATA_PATH = "Mall_Customers.csv"

df = pd.read_csv(DATA_PATH)

# Standardize column names (edit these to match your actual CSV headers)
df.rename(columns={
    "Annual Income (Rs. Thousands)": "Annual_Income",
    "Spending Score (1-100)": "Spending_Score",
    "Gender": "Gender",
    "Age": "Age"
}, inplace=True)


# 2. Preprocess
# Encode Gender: Male -> 0, Female -> 1
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

features = df[["Age", "Gender", "Annual_Income", "Spending_Score"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


# 3. Elbow method to pick k (optional but good for your report)
inertias = []
K_range = range(1, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(scaled_features)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal k")
plt.savefig("elbow_plot.png")
print("Elbow plot saved as elbow_plot.png")


# 4. Train final K-Means model (pick k based on elbow plot, e.g. 5)
OPTIMAL_K = 5

kmeans = KMeans(n_clusters=OPTIMAL_K, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(scaled_features)

print("Cluster counts:")
print(df["Cluster"].value_counts())


# 5. Save model + scaler for use in the app 
with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved: kmeans_model.pkl, scaler.pkl")