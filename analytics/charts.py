import pandas as pd
import matplotlib.pyplot as plt
def income_vs_spending():
    df = pd.read_csv("data/customers.csv")
    plt.figure(figsize=(9, 6))
    personas = df["Persona"].unique()
    for persona in personas:
        persona_data = df[df["Persona"] == persona]
        plt.scatter(
            persona_data["Income"],
            persona_data["SpendingScore"],
            label=persona,
            s=80
        )
def persona_distribution():
    df = pd.read_csv("data/customers.csv")
    persona_counts = df["Persona"].value_counts()
    plt.figure(figsize=(9, 6))
    bars = plt.bar(
        persona_counts.index,
        persona_counts.values
    )
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            str(int(height)),
            ha="center",
            fontsize=12
        )
    plt.xlabel("Customer Persona")
    plt.ylabel("Number of Customers")
    plt.title("Customer Persona Distribution")
    plt.xticks(rotation=20)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()
persona_distribution()