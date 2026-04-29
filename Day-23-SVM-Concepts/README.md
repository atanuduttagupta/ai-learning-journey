# 🧠 Day 23: Support Vector Machines (SVM)

## 📌 Overview

Support Vector Machine (SVM) is a powerful supervised learning algorithm
used for classification and regression. It focuses on finding the
optimal boundary that maximizes separation between classes.

------------------------------------------------------------------------

## 🎯 Key Concepts

### 1. Hyperplane

A decision boundary that separates different classes.

### 2. Margin

Distance between hyperplane and nearest data points. SVM maximizes this.

### 3. Support Vectors

Critical points closest to boundary that define the model.

------------------------------------------------------------------------

## 🔥 Hinge Loss (Core Idea)

Hinge Loss ensures: - Wrong predictions → high penalty - Correct but
close → still penalized - Correct and far → no penalty

Formula: max(0, 1 - y(wx + b))

------------------------------------------------------------------------

## 🧩 Kernel Trick

Used for non-linear data: - Linear Kernel - Polynomial Kernel - RBF
Kernel

Transforms data into higher dimensions.

------------------------------------------------------------------------

## ⚙️ Hyperparameters

  Parameter   Meaning
  ----------- ------------------------------
  C           Controls margin vs error
  gamma       Controls influence of points
  kernel      Type of transformation
  degree      Polynomial degree

------------------------------------------------------------------------

## ⚖️ SVM vs KNN

  Feature      SVM            KNN
  ------------ -------------- -------
  Training     Slow           Fast
  Prediction   Fast           Slow
  Boundary     Clear margin   Local

------------------------------------------------------------------------

## 💼 Real-World Use Cases

-   Fraud Detection (Banking)
-   Spam Detection
-   Image Classification
-   Medical Diagnosis

------------------------------------------------------------------------

## ⚠️ Limitations

-   Slow for large datasets
-   Requires feature scaling
-   Sensitive to hyperparameters

------------------------------------------------------------------------

## 🧑‍💻 Sample Code

``` python
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = SVC(kernel='rbf', C=1)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
```

------------------------------------------------------------------------

## 🚀 Key Takeaway

> SVM is not about just separating data --- it is about finding the
> safest and most confident boundary.

------------------------------------------------------------------------

## 📁 Project Structure

    Day-23-SVM/
    │── svm_notebook.ipynb
    │── solution.py
    │── README.md

------------------------------------------------------------------------

## 🔗 Next Steps

-   Try different kernels
-   Tune C and gamma
-   Visualize decision boundary
-   Build fraud detection mini project
