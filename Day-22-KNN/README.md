# 🚀 Day 22: K-Nearest Neighbors (KNN)

## 📌 Overview
This project is part of my AI learning journey, focusing on **K-Nearest Neighbors (KNN)** — a powerful, intuitive, and widely used machine learning algorithm.

This notebook is **theory-heavy + hands-on**, designed to build deep understanding and practical intuition.

---

## 🧠 Key Concepts Covered

### 1. What is KNN?
- Lazy learning algorithm (no training phase)
- Instance-based learning
- Works on similarity (distance-based)

---

### 2. Distance Metrics

#### Euclidean Distance
- Straight-line distance
- Formula: sqrt(sum((x - y)^2))

#### Manhattan Distance
- Grid-based distance
- Formula: sum(|x - y|)

#### Minkowski Distance
- Generalized distance
- p = 1 → Manhattan, p = 2 → Euclidean

#### Cosine Similarity
- Measures angle between vectors
- Used in NLP, embeddings

---

### 3. Choosing K
- Small K → Overfitting
- Large K → Underfitting
- Rule of thumb: K ≈ sqrt(N)
- Best practice: Cross-validation

---

### 4. Feature Scaling
- Critical for distance-based models
- Techniques:
  - Standardization (Z-score)
  - Normalization (Min-Max)

---

### 5. Decision Boundary
- KNN creates non-linear decision boundaries
- Smaller K → complex boundary
- Larger K → smoother boundary

---

### 6. Classification vs Regression
- Classification → majority voting
- Regression → averaging

---

### 7. Weighted KNN
- Closer neighbors have higher influence
- Weight = 1 / distance
- Improves prediction accuracy

---

### 8. Curse of Dimensionality
- Distance becomes meaningless in high dimensions
- KNN performance degrades

---

### 9. Computational Complexity
- Training: O(1)
- Prediction: O(N × D)

---

### 10. Optimizations
- KD Tree
- Ball Tree
- Approximate Nearest Neighbors (ANN)

---

### 11. Limitations
- Slow for large datasets
- Sensitive to noise
- Requires scaling
- Poor in high-dimensional data

---

## 🏦 Real-World Use Case: Fraud Detection

KNN can be used to:
- Compare new transactions with past transactions
- Identify similar fraud patterns
- Classify transactions as fraud/non-fraud

---

## 🧪 Hands-on Implementations

- Distance calculations (manual)
- KNN classification & regression
- Weighted KNN
- Feature scaling impact
- K selection experiments
- Curse of dimensionality demo

---

## 📂 Project Structure

```
Day-22-KNN/
│
├── notebook.ipynb
├── solution.py
├── README.md
```

---

## 🎯 Key Takeaways

- KNN is simple but powerful
- Distance metric choice is critical
- Scaling is mandatory
- Works well for small to medium datasets
- Not ideal for high-dimensional data

---

## 🔥 Author Note

This project is part of my **AI learning journey (Day 22)** where I focus on:
- Deep understanding
- Real-world applications (BFSI focus)
- Building production-ready intuition

---

## ⭐ If you found this useful
Feel free to ⭐ the repo or connect with me!
