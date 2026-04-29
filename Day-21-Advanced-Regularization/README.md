# 📘 Day 21: Regularization (Lasso, Ridge, ElasticNet)

## 🧠 Overview
This project explores **Regularization in Machine Learning**, focusing on:
- Lasso (L1 Regularization)
- Ridge (L2 Regularization)
- ElasticNet (Combination of L1 + L2)
- Penalty concept
- Lambda (λ) intuition
- Hands-on experiments comparing models

---

## 🔥 Why Regularization?

In real-world datasets, models often:
- Learn noise ❌
- Overfit training data ❌

👉 Regularization helps:
- Reduce model complexity
- Improve generalization

---

## 🧮 General Formula

Loss Function:

Loss = Error + λ × Penalty

Where:
- Error → Prediction error
- Penalty → Model complexity
- λ → Strength of regularization

---

## 🔵 Ridge Regression (L2)

Penalty:
Σ w²

### Key Characteristics:
- Shrinks weights
- Keeps all features
- Handles multicollinearity well

### Intuition:
> “All features matter, but don’t trust any too much.”

---

## 🔴 Lasso Regression (L1)

Penalty:
Σ |w|

### Key Characteristics:
- Forces some weights to zero
- Performs feature selection

### Intuition:
> “Keep only the most important features.”

---

## 🟣 ElasticNet

Combination:

Loss = Error + λ₁|w| + λ₂w²

### Key Characteristics:
- Combines L1 + L2
- Removes noise features
- Keeps correlated features stable

### Intuition:
> “Remove noise like Lasso, stabilize like Ridge.”

---

## ⚖️ Comparison

| Model | Strength |
|------|--------|
| Linear | No regularization |
| Ridge | Stability |
| Lasso | Feature selection |
| ElasticNet | Balanced approach |

---

## 📊 Key Learnings from Experiments

### ✔️ When Lasso Wins
- Sparse data (few useful features)
- Many irrelevant features

### ✔️ When Ridge Wins
- Correlated features
- All features useful

### ✔️ When ElasticNet Helps
- Data has BOTH:
  - Correlation
  - Noise features

---

## 🧪 Hands-on Summary

We tested:
- Linear Regression
- Ridge
- Lasso
- ElasticNet

And compared:
- Mean Squared Error (MSE)
- Coefficients
- Feature selection behavior

---

## ⚠️ Important Insight

> ElasticNet is NOT always the best model.

It performs best when:
- Lasso removes too much
- Ridge keeps too much

---

## 🧠 Final Intuition

- Ridge → “Shrink weights”
- Lasso → “Kill weights”
- ElasticNet → “Balance both”

---

## 🚀 Next Steps

- Plot coefficient paths
- Tune λ and l1_ratio
- Apply on real datasets (fraud detection, credit risk)

---

## ✍️ Author Note

This notebook is part of my **AI Learning Journey** focusing on building strong ML fundamentals with real intuition and hands-on experiments.

---
