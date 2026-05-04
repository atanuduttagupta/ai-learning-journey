# 🌲 Random Forest — Complete Theory Guide

---

## 🧠 What is Random Forest?

Random Forest is an **ensemble learning algorithm** that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

Instead of relying on a single tree, it builds a **forest of trees**, each trained on different subsets of data and features.

👉 Core Idea: *Wisdom of crowds*

---

## 🌱 Bootstrap Sampling

Bootstrap sampling creates multiple datasets using **sampling with replacement**.

- Each dataset is same size as original
- ~63% unique samples
- ~37% Out-of-Bag (OOB)

### 📐 Insight
Each tree sees a **different version of reality**, creating diversity.

---

## 🌳 Bagging (Bootstrap Aggregating)

Multiple trees are trained independently on bootstrap samples.

### 📐 Formula

Classification:
mode(T₁(x), T₂(x), ..., Tₙ(x))

Regression:
(1/n) Σ Tᵢ(x)

👉 Reduces **variance** by averaging predictions.

---

## 🎯 Random Feature Selection

At each split:
- Only a subset of features is considered

### 📐 Typical Values
- Classification → √p
- Regression → p/3

👉 Reduces correlation between trees.

---

## 📊 Out-of-Bag (OOB)

Unused data (~37%) acts as validation.

### 📐 OOB Error
Error = (1/N) Σ I(y ≠ ŷ)

👉 No need for separate validation split.

---

## ⚙️ Hyperparameters

| Parameter | Meaning |
|----------|--------|
| n_estimators | Number of trees |
| max_depth | Maximum depth |
| min_samples_split | Min samples to split |
| min_samples_leaf | Min samples in leaf |
| max_features | Features per split |
| bootstrap | Use bootstrap sampling |

---

## 📉 Why Random Forest Works

Variance reduction:

Var(ensemble) ≈ (1/n) × Var(single tree)

👉 More trees → lower variance (until plateau)

---

## 🏦 Real-Life Use Case (Fraud Detection)

- Detects multiple fraud patterns
- Reduces false negatives
- Handles non-linear behavior

---

## ✅ Advantages

- High accuracy & stability  
- Handles non-linear data  
- Robust to noise  

---

## ⚠️ Limitations

- Less interpretable  
- Computationally expensive  
- Diminishing returns  

---

## 💡 Final Insight

Random Forest =  
Bootstrap (diversity) + Bagging (stability) + Feature Randomness (independence)

👉 Turns weak learners into a strong ensemble.
