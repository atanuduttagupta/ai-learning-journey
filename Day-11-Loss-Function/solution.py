"""
📘 Day 11: Loss Functions - solution.py

Covers:
- Regression Loss: MSE, MAE, Huber
- Classification Loss: Log Loss, Hinge Loss
- Outlier experiment
"""

import numpy as np


# =========================================================
# 📉 REGRESSION LOSSES
# =========================================================

def mse(y_true, y_pred):
    """
    Mean Squared Error
    Penalizes large errors heavily
    """
    return np.mean((y_true - y_pred) ** 2)


def mae(y_true, y_pred):
    """
    Mean Absolute Error
    Treats all errors equally
    """
    return np.mean(np.abs(y_true - y_pred))


def huber(y_true, y_pred, delta=50):
    """
    Huber Loss
    Combines MSE (small errors) + MAE (large errors)
    """
    error = y_true - y_pred

    is_small_error = np.abs(error) <= delta

    squared_loss = 0.5 * (error ** 2)
    linear_loss = delta * (np.abs(error) - 0.5 * delta)

    return np.mean(np.where(is_small_error, squared_loss, linear_loss))


# =========================================================
# 📊 CLASSIFICATION LOSSES
# =========================================================

def log_loss(y_true, y_pred):
    """
    Binary Cross Entropy (Log Loss)
    Penalizes confident wrong predictions heavily
    """
    epsilon = 1e-15  # for numerical stability

    # Avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    return -np.mean(
        y_true * np.log(y_pred) +
        (1 - y_true) * np.log(1 - y_pred)
    )


def hinge_loss(y_true, y_pred):
    """
    Hinge Loss (used in SVM)
    y_true must be in {-1, +1}
    """
    return np.mean(np.maximum(0, 1 - y_true * y_pred))


# =========================================================
# 🧪 TESTING / DEMO
# =========================================================

if __name__ == "__main__":

    print("===== REGRESSION LOSSES =====")

    y_true = np.array([100, 200, 300])
    y_pred = np.array([110, 190, 400])

    print("MSE:", mse(y_true, y_pred))
    print("MAE:", mae(y_true, y_pred))
    print("Huber:", huber(y_true, y_pred))

    print("\n===== OUTLIER EXPERIMENT =====")

    y_true_out = np.array([100, 200, 300, 10000])
    y_pred_out = np.array([110, 190, 400, 0])

    print("MSE with outlier:", mse(y_true_out, y_pred_out))
    print("MAE with outlier:", mae(y_true_out, y_pred_out))
    print("Huber with outlier:", huber(y_true_out, y_pred_out))

    print("\n===== CLASSIFICATION LOSSES =====")

    # Log Loss (0/1 labels)
    y_true_cls = np.array([1, 0, 1])
    y_pred_cls = np.array([0.9, 0.2, 0.1])

    print("Log Loss:", log_loss(y_true_cls, y_pred_cls))

    # Hinge Loss (-1/+1 labels)
    y_true_hinge = np.array([1, -1, 1])
    y_pred_hinge = np.array([0.8, -0.5, -0.2])

    print("Hinge Loss:", hinge_loss(y_true_hinge, y_pred_hinge))