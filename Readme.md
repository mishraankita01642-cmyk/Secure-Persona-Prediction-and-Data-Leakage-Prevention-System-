# SecurePersonaPrediction

## Customer Persona Prediction and Analytics Dashboard

SecurePersonaPrediction is a Python-based customer analytics project that analyzes customer income and spending behavior and classifies customers into different personas.

The project provides customer insights through data analysis, visualizations, prediction history, recommendations, and an interactive analytics dashboard.

## Features

- Customer data analysis
- Customer persona classification
- Income vs Spending visualization
- Customer persona distribution chart
- Prediction history tracking
- Personalized recommendations
- PDF report generation
- Interactive Customer Analytics Dashboard

## Customer Personas

The system identifies customers into four categories:

1. High-Value Customer
2. Budget Customer
3. Potential Customer
4. Impulsive Spender

## Technologies Used

- Python
- Pandas
- Matplotlib
- CustomTkinter
- Tkinter
- ReportLab
- CSV

## Project Structure

```text
SecurePersonaPrediction/
│
├── analytics/
│   ├── charts.py
│   ├── dashboard.py
│   ├── data_analysis.py
│   └── history.py
│
├── data/
│   ├── customers.csv
│   └── prediction_history.csv
│
├── recommendation/
│   └── recommendation.py
│
├── reports/
│   ├── report_generator.py
│   ├── test_report.py
│   └── C001_persona_report.pdf
│
├── main.py
└── .gitignore