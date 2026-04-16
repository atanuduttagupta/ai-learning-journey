"""
Day 10: Gradient Descent, Loss Function & Optimization

This script demonstrates:
- Loss Function (MSE)
- Gradient calculation
- Gradient Descent from scratch
- Learning rate behavior

Author: Atanu (AI Learning Journey)
"""

import numpy as np


# -------------------------------
# 1. LOSS FUNCTION (MSE)
# -------------------------------
def mean_squared_error(y_true, y_pred):
    """
    Computes Mean Squared Error

    MSE = average((y_true - y_pred)^2)
    """
    return np.mean((y_true - y_pred) ** 2)


# -------------------------------
# 2. GRADIENT FUNCTION
# -------------------------------
def compute_gradient(X, y, y_pred):
    """
    Computes gradient of loss w.r.t weight (w)

    Formula:
    gradient = -2 * mean(X * (y - y_pred))
    """
    return -2 * np.mean(X * (y - y_pred))


# -------------------------------
# 3. GRADIENT DESCENT FUNCTION
# -------------------------------
def gradient_descent(X, y, learning_rate=0.01, epochs=100):
    """
    Performs Gradient Descent to learn weight (w)

    Steps:
    1. Initialize weight
    2. Predict output
    3. Compute loss
    4. Compute gradient
    5. Update weight
    """

    # Initialize weight
    w = 0

    print("Starting Gradient Descent...\n")

    for epoch in range(epochs):

        # Step 1: Prediction
        y_pred = w * X

        # Step 2: Loss calculation
        loss = mean_squared_error(y, y_pred)

        # Step 3: Gradient calculation
        gradient = compute_gradient(X, y, y_pred)

        # Step 4: Update rule
        w = w - learning_rate * gradient

        # Print progress
        if epoch % 10 == 0:
            print(f"Epoch {epoch}")
            print(f"  Loss     : {loss:.4f}")
            print(f"  Gradient : {gradient:.4f}")
            print(f"  Weight   : {w:.4f}")
            print("-" * 30)

    return w


# -------------------------------
# 4. MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":

    # Sample Data (True relationship: y = 2x)
    X = np.array([1, 2, 3, 4])
    y = np.array([2, 4, 6, 8])

    # Run Gradient Descent
    final_weight = gradient_descent(X, y, learning_rate=0.01, epochs=100)

    print("\nFinal Learned Weight:", round(final_weight, 4))


# -------------------------------
# 5. EXPERIMENT SECTION
# -------------------------------
"""
Try changing:

1. Learning Rate:
   - 0.1   → Fast but may overshoot
   - 0.0001 → Very slow

2. Initial Weight:
   Change w = 10 inside function

Observe:
- Does loss decrease?
- Does it converge to ~2?

This builds real intuition.
"""