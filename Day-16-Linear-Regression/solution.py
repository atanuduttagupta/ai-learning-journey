# =========================================
# Day 16: Regression Concepts - solution.py
# =========================================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# =========================================================
# 🔹 1. SIMPLE LINEAR REGRESSION (Salary vs Experience)
# =========================================================

print("\n===== SIMPLE LINEAR REGRESSION =====")

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([30000, 40000, 50000, 60000, 70000])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("Test MSE:", mean_squared_error(y_test, y_pred))


# =========================================================
# 🔹 2. MULTIPLE LINEAR REGRESSION (House Price)
# =========================================================

print("\n===== MULTIPLE LINEAR REGRESSION =====")

X = np.array([
    [1000, 1, 2],
    [1200, 1, 2],
    [1500, 2, 3],
    [1700, 2, 3],
    [2000, 2, 4],
    [2200, 3, 4],
    [2500, 3, 4],
    [2700, 3, 5]
])

y = np.array([50, 60, 80, 90, 120, 135, 150, 165])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

print("Weights:", model.coef_)
print("Intercept:", model.intercept_)
print("Train MSE:", mean_squared_error(y_train, y_train_pred))
print("Test MSE:", mean_squared_error(y_test, y_test_pred))

# Plot
plt.figure()
plt.scatter(y_train, y_train_pred, label="Train")
plt.scatter(y_test, y_test_pred, label="Test")

min_val = min(y.min(), y_train_pred.min(), y_test_pred.min())
max_val = max(y.max(), y_train_pred.max(), y_test_pred.max())

plt.plot([min_val, max_val], [min_val, max_val], linestyle='--')

plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Multiple Regression: Actual vs Predicted")
plt.legend()
plt.show()


# =========================================================
# 🔹 3. POLYNOMIAL REGRESSION
# =========================================================

print("\n===== POLYNOMIAL REGRESSION =====")

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

y_train_pred = model.predict(X_train_poly)
y_test_pred = model.predict(X_test_poly)

print("Train MSE:", mean_squared_error(y_train, y_train_pred))
print("Test MSE:", mean_squared_error(y_test, y_test_pred))

# Plot smooth curve
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = model.predict(X_range_poly)

plt.figure()
plt.scatter(X_train, y_train, label="Train")
plt.scatter(X_test, y_test, label="Test")
plt.plot(X_range, y_range_pred, label="Polynomial Fit")

plt.title("Polynomial Regression")
plt.legend()
plt.show()


# =========================================================
# 🔹 4. RIDGE & LASSO REGRESSION
# =========================================================

print("\n===== RIDGE vs LASSO =====")



# Sample data
X = np.random.rand(100, 3)
y = X @ np.array([10, 20, 30]) + np.random.randn(100)*2

noise = np.random.rand(100, 1)
X_new = np.hstack([X, noise])

# Scaling is IMPORTANT here
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_new)

from sklearn.linear_model import LinearRegression

linear = LinearRegression()
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_scaled, y)
lasso.fit(X_scaled, y)
linear.fit(X_scaled, y)

print("Linear Coefficients:", linear.coef_)
print("Ridge Coefficients :", ridge.coef_)
print("Lasso Coefficients :", lasso.coef_)

print("\n--- Shrinkage Comparison ---")
for i in range(len(linear.coef_)):
    print(f"Feature {i}:")
    print(f"  Linear: {linear.coef_[i]:.3f}")
    print(f"  Ridge : {ridge.coef_[i]:.3f}")
    print(f"  Lasso : {lasso.coef_[i]:.3f}")

zero_weights = sum(lasso.coef_ == 0)
print("\nNumber of features removed by Lasso:", zero_weights)