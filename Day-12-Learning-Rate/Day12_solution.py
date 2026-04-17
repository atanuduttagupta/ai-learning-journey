
# Day 12: Learning Rate, Optimization & Backpropagation
# Clean solution script (GitHub-ready)

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Generate Data
# -----------------------------
np.random.seed(42)

X = np.random.rand(100)
y_true = 3 * X + 2   # True relationship

# -----------------------------
# 2. Initialize Parameters
# -----------------------------
w = 0.0
b = 0.0
lr = 0.1
epochs = 50

losses = []

# -----------------------------
# 3. Training Loop (Gradient Descent)
# -----------------------------
for i in range(epochs):
    # Forward pass
    y_pred = w * X + b

    # Loss (MSE)
    loss = np.mean((y_pred - y_true) ** 2)

    # Gradients
    grad_w = np.mean(2 * (y_pred - y_true) * X)
    grad_b = np.mean(2 * (y_pred - y_true))

    # Update parameters
    w -= lr * grad_w
    b -= lr * grad_b

    losses.append(loss)

    print(f"Epoch {i+1}: w={w:.4f}, b={b:.4f}, loss={loss:.4f}")

# -----------------------------
# 4. Final Results
# -----------------------------
print("\nFinal Learned Parameters:")
print(f"w ≈ {w:.4f} (Expected ~3)")
print(f"b ≈ {b:.4f} (Expected ~2)")

# -----------------------------
# 5. Plot Loss Convergence
# -----------------------------
plt.plot(losses)
plt.title("Loss Convergence")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()

# -----------------------------
# 6. Visualize Predictions
# -----------------------------
plt.scatter(X, y_true, label="True Data")
plt.scatter(X, w*X + b, label="Predictions")
plt.legend()
plt.title("Model Fit")
plt.show()
