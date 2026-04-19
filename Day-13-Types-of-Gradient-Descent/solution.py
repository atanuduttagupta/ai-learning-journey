"""
Day 13: Types of Gradient Descent (Level 2) - solution.py
"""

import numpy as np

def make_dataset(n=1000, seed=42):
    np.random.seed(seed)
    X = np.random.rand(n) * 100.0
    noise = np.random.normal(0, 10, n)
    y = 0.5 * X + 20 + noise
    return X, y

def compute_loss(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)

def mini_batch_gd_shuffle(X, y, lr=1e-4, batch_size=32, epochs=20):
    w, b = 0.0, 0.0
    losses = []
    n = len(X)

    for _ in range(epochs):
        idx = np.random.permutation(n)
        Xs, ys = X[idx], y[idx]

        for i in range(0, n, batch_size):
            Xb = Xs[i:i + batch_size]
            yb = ys[i:i + batch_size]

            y_pred = w * Xb + b
            grad_w = np.mean(2 * (y_pred - yb) * Xb)
            grad_b = np.mean(2 * (y_pred - yb))

            w -= lr * grad_w
            b -= lr * grad_b

        losses.append(compute_loss(w * X + b, y))

    return w, b, losses

def main():
    X, y = make_dataset()
    w, b, losses = mini_batch_gd_shuffle(X, y)
    print("Mini-batch -> w:", w, "b:", b)

if __name__ == "__main__":
    main()
