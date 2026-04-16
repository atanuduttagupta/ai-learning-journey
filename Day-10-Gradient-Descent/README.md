# 🚀 Day 10 — Gradient Descent & Optimization

## 📌 Overview
This project is part of my AI Learning Journey where I explore core Machine Learning concepts with hands-on implementation.

In this project, I implemented Gradient Descent from scratch to understand how models learn by minimizing error.

---

## 🧠 Concepts Covered

- Loss Function (Squared Error, MSE)
- Gradient (rate of change of loss)
- Gradient Descent (optimization algorithm)
- Learning Rate (step size control)
- Local vs Global Minima

---

## 🔍 Problem Statement

Given a simple dataset:
y = 2x

The goal is to learn the weight (w) using Gradient Descent instead of solving it directly.

---

## ⚙️ Approach

1. Initialize weight
2. Predict output: y_pred = w * X
3. Compute loss (MSE)
4. Compute gradient
5. Update weight:
   w = w - learning_rate * gradient
6. Repeat until convergence

---

## 🧪 Example Output

Epoch 0  → Loss high → Weight adjusting  
Epoch 50 → Loss lower → Weight approaching 2  
Epoch 100 → Loss near 0 → Weight ≈ 2  

---

## 📂 Project Structure

Day-10-Gradient-Descent/
│
├── Day10_Gradient_Descent.ipynb
├── solution.py
├── README.md

---

## 💡 Key Learnings

- Models improve by minimizing error step-by-step
- Gradient shows direction of improvement
- Learning rate controls speed
- Optimization is core to Machine Learning

---

## 💼 Real-World Applications

- Recommendation systems
- Fraud detection
- Price prediction
- Autonomous systems

---

## 🔬 Experiments to Try

- Change learning rate (0.1 vs 0.0001)
- Change initial weight

---

## 🧑‍💻 Tech Stack

- Python
- NumPy

---

## ⭐ Final Thought

Gradient Descent is the reason machines can learn and improve.
