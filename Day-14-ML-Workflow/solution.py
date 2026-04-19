# Day 14: Machine Learning Workflow (End-to-End)

# ------------------------------------------------

# This script follows a full ML pipeline:

# Problem → Data → Preprocessing → Feature Engineering → Training → Prediction

# ================================

# 1. Import Libraries

# ================================

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ================================

# 2. Data Generation (Synthetic BFSI Data)

# ================================

np.random.seed(42)

# Simulating customer data

income = np.random.randint(20000, 100000, 100)
loan = np.random.randint(5000, 50000, 100)

# Risk formula (hidden pattern)

risk = (loan / income) + np.random.normal(0, 0.05, 100)

# Create DataFrame

df = pd.DataFrame({
"income": income,
"loan": loan,
"risk": risk
})

print("Initial Data Sample:")
print(df.head())

# ================================

# 3. Data Preprocessing

# ================================

# Introduce missing values (simulation)

df.loc[5, "income"] = None

print("\nData with Missing Value:")
print(df.head(10))

# Handle missing values

df["income"] = df["income"].fillna(df["income"].mean())

print("\nAfter Handling Missing Values:")
print(df.head(10))

# ================================

# 4. Feature Engineering

# ================================

# Create new feature: loan-to-income ratio

df["loan_to_income"] = df["loan"] / df["income"]

print("\nAfter Feature Engineering:")
print(df.head())

# ================================

# 5. Prepare Data for Model

# ================================

X = df[["income", "loan", "loan_to_income"]]
y = df["risk"]

# ================================

# 6. Model Training

# ================================

model = LinearRegression()
model.fit(X, y)

print("\nModel Training Completed")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# ================================

# 7. Prediction

# ================================

# Example: New customer

new_customer = [[50000, 20000, 20000/50000]]

prediction = model.predict(new_customer)

print("\nPrediction for New Customer:")
print("Risk Score:", prediction[0])

# ================================

# 8. Business Interpretation

# ================================

risk_score = prediction[0]

if risk_score < 0.3:
decision = "APPROVE"
elif risk_score < 0.6:
decision = "REVIEW"
else:
decision = "REJECT"

print("\nLoan Decision:", decision)

# ================================

# 9. Key Takeaways (Printed)

# ================================

print("\n--- Key Insights ---")
print("1. ML is a pipeline, not just a model")
print("2. Feature engineering (loan_to_income) is critical")
print("3. Model predicts continuous risk score")
print("4. Business logic converts score → decision")

# ================================

# END

# ================================
