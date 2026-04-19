# Day 14: Machine Learning Workflow (End-to-End)

## 📌 Overview
This project demonstrates a complete **Machine Learning Workflow** using a **Credit Risk Prediction** example (BFSI domain).

It covers the full pipeline:
> Problem → Data → Preprocessing → Feature Engineering → Model Training → Prediction → Business Decision

---

## 🧠 Key Concepts Covered

- Problem Definition
- Data Collection (Synthetic)
- Data Preprocessing (Handling Missing Values)
- Feature Engineering (Loan-to-Income Ratio)
- Model Training (Linear Regression)
- Prediction & Interpretation
- Mapping Model Output → Business Decision

---

## 🏦 Real-World Use Case

**Credit Risk Prediction System**

We simulate a banking scenario where:
- Customers have income & loan amount
- Model predicts a **risk score**
- Business logic converts score → loan decision

---

## ⚙️ Project Structure

```
Day-14-ML-Workflow/
│
├── Day14_ML_Workflow_Advanced.ipynb
├── solution.py
└── README.md
```

---

## 🚀 How It Works

### 1. Data Generation
Synthetic customer data:
- Income (₹20K – ₹1L)
- Loan amount (₹5K – ₹50K)

### 2. Hidden Pattern
```
risk ≈ loan / income
```

### 3. Feature Engineering
```
loan_to_income = loan / income
```

This improves model learning significantly.

---

## 🤖 Model Used

- **Linear Regression**

Why?
- Simple
- Interpretable
- Good for learning workflow

---

## 📈 Sample Prediction

Input:
```
Income = 50,000
Loan = 20,000
```

Output:
```
Risk Score ≈ 0.39
```

---

## 🧠 Business Decision Logic

| Risk Score | Decision |
|----------|--------|
| < 0.3 | APPROVE |
| 0.3 – 0.6 | REVIEW |
| > 0.6 | REJECT |

---

## 🔥 Key Learnings

- ML is **not just model training**
- **Feature engineering = real power**
- Model output must be converted into **business decisions**
- Synthetic data helps in understanding workflow

---

## ⚠️ Limitations

- Uses synthetic data (not real banking data)
- Linear model (real systems use advanced models)
- No train-test split (covered in Day 15)

---

## 🚀 Next Steps (Day 15)

- Train-Test Split
- Overfitting vs Underfitting
- Model Evaluation (RMSE)
- Logistic Regression (for classification)

---

## 🧑‍💻 Author

AI Learning Journey – Day 14  
Building in public 🚀

---

## ⭐ If you found this useful
Give a ⭐ on GitHub and follow the journey!
