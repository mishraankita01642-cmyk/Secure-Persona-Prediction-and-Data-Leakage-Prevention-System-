import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import sys
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from history import get_prediction_history
df = pd.read_csv("data/customers.csv")
total_customers = len(df)
average_income = df["Income"].mean()
average_spending = df["SpendingScore"].mean()
persona_counts = df["Persona"].value_counts()
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Customer Analytics Dashboard")
app.geometry("1200x750")
title = ctk.CTkLabel(
    app,
    text="CUSTOMER ANALYTICS DASHBOARD",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)
stats_frame = ctk.CTkFrame(app)
stats_frame.pack(
    fill="x",
    padx=30,
    pady=10
)
total_label = ctk.CTkLabel(
    stats_frame,
    text=f"Total Customers\n{total_customers}",
    font=("Arial", 20, "bold")
)
total_label.grid(
    row=0,
    column=0,
    padx=50,
    pady=20
)
income_label = ctk.CTkLabel(
    stats_frame,
    text=f"Average Income\nRs. {average_income:,.0f}",
    font=("Arial", 20, "bold")
)
income_label.grid(
    row=0,
    column=1,
    padx=50,
    pady=20
)
spending_label = ctk.CTkLabel(
    stats_frame,
    text=f"Average Spending\n{average_spending:.2f}",
    font=("Arial", 20, "bold")
)
spending_label.grid(
    row=0,
    column=2,
    padx=50,
    pady=20
)
graph_frame = ctk.CTkFrame(app)
graph_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)
fig, (ax1, ax2) = plt.subplots(
    1,
    2,
    figsize=(12, 5)
)
for persona in df["Persona"].unique():
    persona_data = df[df["Persona"] == persona]
    ax1.scatter(
        persona_data["Income"],
        persona_data["SpendingScore"],
        label=persona,
        s=60
    )
ax1.set_title("Income vs Spending")
ax1.set_xlabel("Annual Income")
ax1.set_ylabel("Spending Score")
ax1.grid(True)
ax1.legend(fontsize=7)
bars = ax2.bar(
    persona_counts.index,
    persona_counts.values
)
ax2.set_title("Persona Distribution")
ax2.set_xlabel("Customer Persona")
ax2.set_ylabel("Number of Customers")
ax2.tick_params(
    axis="x",
    rotation=25
)
for bar in bars:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom"
    )
ax2.grid(axis="y")
fig.tight_layout()
canvas = FigureCanvasTkAgg(
    fig,
    master=graph_frame
)
canvas.draw()
canvas.get_tk_widget().pack(
    fill="both",
    expand=True
)
history_title = ctk.CTkLabel(
    app,
    text="PREDICTION HISTORY",
    font=("Arial", 22, "bold")
)
history_title.pack(pady=(15, 5))
history_frame = ctk.CTkFrame(app)
history_frame.pack(
    fill="x",
    padx=30,
    pady=5
)
history = get_prediction_history()
headers = [
    "Customer ID",
    "Income",
    "Spending Score",
    "Persona"
]
for column, header in enumerate(headers):
    label = ctk.CTkLabel(
        history_frame,
        text=header,
        font=("Arial", 14, "bold")
    )
    label.grid(
        row=0,
        column=column,
        padx=25,
        pady=8
    )
for row_index, row in history.iterrows():
    values = [
        row["CustomerID"],
        f"Rs. {row['Income']:,.0f}",
        row["SpendingScore"],
        row["Persona"]
    ]
    for column_index, value in enumerate(values):
        label = ctk.CTkLabel(
            history_frame,
            text=str(value),
            font=("Arial", 13)
        )
        label.grid(
            row=row_index + 1,
            column=column_index,
            padx=25,
            pady=5
        )
def generate_pdf_report():
    try:
        subprocess.run(
            [sys.executable, "reports/test_report.py"],
            check=True
        )

        pdf_path = os.path.abspath(
            "reports/C001_persona_report.pdf"
        )

        if os.path.exists(pdf_path):
            os.startfile(pdf_path)

    except Exception as e:
        print("Error generating report:", e)
report_button = ctk.CTkButton(
    app,
    text="GENERATE PDF REPORT",
    command=generate_pdf_report,
    font=("Arial", 16, "bold"),
    height=45,
    width=250
)
report_button.pack(pady=15)
app.mainloop()