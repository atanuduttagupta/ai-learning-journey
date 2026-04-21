# 📘 Day 15: Supervised Learning (Theory + Hands-on)

# =========================================================
# 🧠 SECTION 1: INTRODUCTION (THEORY HEAVY)
# =========================================================

"""
Supervised Learning is one of the most fundamental paradigms in Machine Learning.

Definition:
------------
Supervised Learning is a type of learning where the model is trained on labeled data.

This means:
    Input (X) ---> Output (y) is already known

Goal:
------
Learn a mapping function f such that:
    y = f(X)

Real-world analogy:
-------------------
Think of it like learning with a teacher:
- Teacher gives questions (inputs)
- Teacher also gives correct answers (labels)
- You learn the pattern

In ML:
- Model = student
- Data = teacher

"""

# =========================================================
# 📊 SECTION 2: TYPES OF SUPERVISED LEARNING
# =========================================================

"""
1. Regression
-------------
- Output is continuous (numeric)
- Examples:
    - House price prediction
    - Salary prediction

2. Classification
------------------
- Output is categorical
- Examples:
    - Spam detection (Spam / Not Spam)
    - Fraud detection (Fraud / Not Fraud)

"""

# =========================================================
# ⚙️ SECTION 3: HOW LEARNING WORKS (VERY IMPORTANT)
# =========================================================

"""
Training Loop:
--------------
1. Model makes prediction
2. Compare with actual value
3. Compute loss (error)
4. Update model parameters
5. Repeat

This is the core of ALL machine learning systems.
"""

# =========================================================
# 📦 SECTION 4: IMPORT LIBRARIES
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

# =========================================================
# 🧪 SECTION 5: REGRESSION HANDS-ON (Salary Prediction)
# =========================================================

"""
Problem:
--------
Predict salary based on years of experience

"""

# Create dataset
np.random.seed(42)
experience = np.random.randint(1, 10, 50)
salary = experience * 5000 + np.random.randint(-2000, 2000, 50)

# Convert to DataFrame
df_reg = pd.DataFrame({
    'Experience': experience,
    'Salary': salary
})

print(df_reg.head())

# Split data
X = df_reg[['Experience']]
y = df_reg['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model_reg = LinearRegression()
model_reg.fit(X_train, y_train)

# Predictions
y_pred = model_reg.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# Visualization
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.title("Regression: Experience vs Salary")
plt.show()

# =========================================================
# 🧪 SECTION 6: CLASSIFICATION HANDS-ON (Loan Approval)
# =========================================================

"""
Problem:
--------
Predict loan approval (0/1) based on income & credit score

"""

# Create dataset
income = np.random.randint(20000, 100000, 100)
credit_score = np.random.randint(300, 850, 100)

# Rule-based labels (simulated reality)
approval = (income > 50000) & (credit_score > 600)
approval = approval.astype(int)

# DataFrame
df_clf = pd.DataFrame({
    'Income': income,
    'CreditScore': credit_score,
    'Approved': approval
})

print(df_clf.head())

# Features & target
X = df_clf[['Income', 'CreditScore']]
y = df_clf['Approved']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Fit on training data only
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

# Train model
model_clf = LogisticRegression()
model_clf.fit(X_train, y_train)

# Predict
y_pred = model_clf.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# =========================================================
# 📈 SECTION 7: INTERPRETATION (IMPORTANT)
# =========================================================

"""
Regression:
-----------
- Model learns relationship between experience and salary
- Slope indicates salary increase per year

Classification:
---------------
- Model learns decision boundary
- Separates Approved vs Not Approved

"""

# =========================================================
# 🧠 SECTION 8: KEY LEARNINGS
# =========================================================

"""
1. Supervised learning uses labeled data
2. Two types: Regression & Classification
3. Model learns patterns, not logic
4. Data quality is critical
5. Evaluation metrics matter

"""

# =========================================================
# 🚀 SECTION 9: MINI PROJECT
# =========================================================

"""
Build your own:
---------------
1. Add more features (age, loan amount)
2. Improve model accuracy
3. Try different algorithms
4. Visualize decision boundary

"""

print("\n✅ Day 15 Completed Successfully!")
