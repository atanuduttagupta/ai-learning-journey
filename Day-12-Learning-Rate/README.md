# Day 12: Learning Rate, Optimization Intuition & Backpropagation

## 📌 Overview
This project builds a **strong intuition of how models learn** using gradient descent.  
It covers learning rate behavior, convex vs non-convex optimization, chain rule, and backpropagation—ending with a small **BFSI-style mini project**.

---

## 🎯 What You’ll Learn
- What **learning rate (η)** does and why it matters  
- Difference between **convex vs non-convex** loss landscapes  
- **Chain rule** as the foundation of backpropagation  
- How **gradients** are computed and used to update parameters  
- Why **vanishing/exploding gradients** happen  
- Practical gradient descent on a **linear regression model**

---

## 🧠 Key Concepts

### Gradient Descent
Updates model parameters to minimize loss:
```
θ = θ - η ∇J(θ)
```

### Mean Squared Error (MSE)
```
L = (y_pred - y_true)^2
```

### Gradient (for Linear Model)
```
grad_w = mean(2 * (y_pred - y_true) * X)
grad_b = mean(2 * (y_pred - y_true))
```

---

## 🧪 Mini Project: Loan Risk Optimization (BFSI)
Simulates predicting a **risk score** using a linear model:

- True relationship: `y = 3X + 2`
- Model learns parameters `w` and `b`
- Uses gradient descent to minimize error

### Results
- Converges close to:
  - `w ≈ 3`
  - `b ≈ 2`
- Loss decreases over iterations 📉

---

## 📊 Outputs
- Loss convergence plot  
- Model predictions vs actual data  
- Parameter updates over epochs  

---

## ⚠️ Key Learnings
- Learning rate too small → slow learning  
- Learning rate too large → divergence  
- Missing bias → model cannot fit data correctly  
- Gradient = **direction of steepest increase**  

---

## 🚀 How to Run

```bash
python Day12_solution.py
```

---

## 📂 Project Structure
```
Day-12/
│── Day12_Learning_Rate_Backprop_Notebook.ipynb
│── Day12_solution.py
│── README.md
```

---

## 🧩 One-Line Summary
**Models learn by adjusting parameters step-by-step using gradients—learning rate decides how fast and how stable this learning is.**

---

## 🔗 Next Steps
- Try different learning rates (`0.01`, `0.5`, `1.0`)
- Add noise to data
- Extend to multiple features

---

## ✍️ Author
Part of the **AI Learning Journey (Day 12)**  
Focused on building intuition before moving to deep learning 🚀
