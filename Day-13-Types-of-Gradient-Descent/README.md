# 🚀 Day 13: Types of Gradient Descent (Level 2)

## 📌 Overview
This project explores different types of Gradient Descent used in Machine Learning:

- Batch Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent (Industry Standard)

The focus is on understanding:
- How each method works
- Trade-offs (speed vs stability)
- Real-world usage

---

## 🧠 Key Concepts

### 1. Batch Gradient Descent
- Uses full dataset
- Stable but slow

### 2. Stochastic Gradient Descent (SGD)
- Uses one sample at a time
- Fast but noisy

### 3. Mini-Batch Gradient Descent
- Uses small batches (e.g., 32 samples)
- Best balance → widely used in industry

---

## ⚙️ Implementation Details

- Synthetic dataset simulating fraud detection
- Linear model: y = wx + b
- Loss function: Mean Squared Error (MSE)
- Gradient computed manually (no libraries like sklearn)

---

## 🔀 Important Technique: Data Shuffling

Each epoch:
- Data is shuffled randomly
- Prevents learning bias from fixed order
- Improves generalization

---

## 📊 Output

The script prints:
- Final values of w (weight)
- Final values of b (bias)

---

## ▶️ How to Run

```bash
python solution.py
```

---

## 🧪 What You Can Experiment With

- Change learning rate (lr)
- Change batch size
- Increase number of epochs
- Add noise to dataset

---

## 🚀 Next Steps

- Implement Optimizers (Adam, RMSProp, Momentum)
- Compare convergence speed
- Add visualization (loss curves)

---

## 💡 Key Takeaway

> Mini-Batch Gradient Descent is the backbone of modern AI training.
