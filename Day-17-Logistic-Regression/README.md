# 📘 Day 17: Logistic Regression (Theory + Hands-On)

## 🚀 Overview

This notebook covers **Classification Concepts and Logistic
Regression**, with both theory and hands-on examples.

------------------------------------------------------------------------

## 🧠 Topics Covered

-   Classification vs Regression
-   Sigmoid Function
-   Decision Boundary & Threshold
-   Types of Logistic Regression:
    -   Binary Logistic Regression
    -   Multinomial Logistic Regression
    -   Ordinal Logistic Regression
    -   Multi-Label Classification
-   One-vs-Rest (OvR) Strategy

------------------------------------------------------------------------

## 💻 Hands-On Implementations

### 🔹 1. Binary Logistic Regression

-   Customer churn prediction
-   Includes scaling + train-test split

### 🔹 2. Multinomial Logistic Regression

-   Iris dataset classification
-   Uses pipeline (scaling + model)

### 🔹 3. Ordinal Logistic Regression

-   Income → Rating prediction
-   Demonstrates ordered categories

### 🔹 4. Multi-Label Classification

-   Movie genre prediction
-   Multiple outputs per sample

------------------------------------------------------------------------

## ⚙️ Techniques Used

-   StandardScaler (Feature Scaling)
-   Pipeline (Production-ready workflow)
-   Train-Test Split
-   MultiOutputClassifier

------------------------------------------------------------------------

## 📊 Key Learnings

-   Logistic Regression outputs probabilities, not direct classes
-   Threshold (0.5) is configurable
-   Scaling improves model performance
-   OvR converts multi-class → multiple binary problems
-   Multi-label problems need different evaluation metrics

------------------------------------------------------------------------

## ⚠️ Important Notes

-   Small datasets can give misleading accuracy
-   Multi-label accuracy is strict (all labels must match)
-   Logistic Regression does not truly handle ordinal relationships

------------------------------------------------------------------------

## 🏦 Real-World Applications

-   Fraud Detection
-   Loan Approval
-   Customer Churn Prediction
-   Recommendation Systems

------------------------------------------------------------------------

## 📈 Next Steps (Day 18)

-   Confusion Matrix
-   Precision / Recall
-   F1 Score
-   ROC Curve

------------------------------------------------------------------------

## 📂 Project Structure

Day-17-Logistic-Regression/ │── Day17_Logistic_Regression_Notebook.ipynb
│── solution.py │── README.md

------------------------------------------------------------------------

## ✍️ Author

Part of AI Learning Journey (330-Day Roadmap)\
Focus: Transitioning into AI/ML with real-world projects
