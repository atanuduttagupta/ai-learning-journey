# 📘 Day 11: Loss Functions Deep Dive

## 🎯 Overview
This project explores the **core loss functions used in Machine Learning**, with a focus on both:
- 📉 Regression Losses
- 📊 Classification Losses

Understanding loss functions is critical because they define **how a model learns** and **what it tries to optimize**.

---

## 🧠 What are Loss Functions?

A loss function measures the **difference between actual values and predicted values**.

👉 In simple terms:
- Model predicts something
- Reality is something else
- Loss = how wrong the model is

---

## 📉 Regression Loss Functions

### 1️⃣ Mean Squared Error (MSE)
- Penalizes large errors heavily
- Sensitive to outliers
- Used in: price prediction, forecasting

### 2️⃣ Mean Absolute Error (MAE)
- Treats all errors equally
- More robust to outliers

### 3️⃣ Huber Loss
- Combines MSE and MAE
- Stable and robust
- Used in: finance, autonomous systems

---

## 📊 Classification Loss Functions

### 4️⃣ Binary Cross Entropy (Log Loss)
- Works with probabilities (0 to 1)
- Penalizes confident wrong predictions
- Used in: fraud detection, medical diagnosis

### 5️⃣ Hinge Loss (SVM)
- Works with labels {-1, +1}
- Focuses on maximizing margin
- Used in: Support Vector Machines

---

## 🔬 Key Experiment: Outliers

We compare how different loss functions behave when **extreme values (outliers)** are introduced.

👉 Observation:
- MSE explodes 🚀
- MAE remains stable
- Huber balances both

---

## 💳 Real-World Application (BFSI)

### Fraud Detection
- Predict probability of fraud
- Use **Log Loss** to penalize incorrect confident predictions

👉 Example:
- Predict fraud = 0.99 → good
- Predict fraud = 0.01 → dangerous ❌

---

## 🧩 Project Structure

```
Day-11-Loss-Functions/
│── notebook.ipynb
│── solution.py
│── README.md
```

---

## 🚀 How to Run

```bash
python solution.py
```

---

## 📌 Key Learnings

- Loss functions drive model learning
- Different problems require different loss functions
- Handling outliers is critical
- Numerical stability (like clipping) is important

---

## 🔥 Future Improvements

- Add visualization of loss curves
- Use real datasets
- Compare model performance across loss functions

---

## 🙌 Author

Part of my **AI Learning Journey**  
Sharing daily progress towards becoming an AI Engineer 🚀
