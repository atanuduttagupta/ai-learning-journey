# 📘 Day 20: Advanced Classification (Theory + Hands-on)

## 🚀 Overview
This project covers advanced classification concepts essential for real-world machine learning systems, especially in domains like fraud detection (BFSI).

---

## 📚 Topics Covered

### 🔹 Train–Test–Validation Split
- Train → Learn patterns  
- Validation → Tune model  
- Test → Final evaluation  
- ⚠️ Avoid data leakage

---

### 🔹 Stratified Split
- Maintains class distribution  
- Critical for imbalanced datasets (e.g., fraud detection)

---

### 🔹 Cross Validation (K-Fold)
- Splits data into K parts  
- Trains on K-1 folds, tests on remaining  
- Reduces variance  
- More reliable performance

---

### 🔹 Threshold Tuning
- Default threshold = 0.5  
- Lower threshold → High Recall  
- Higher threshold → High Precision  

💡 Business-driven decision:
- Fraud detection → prioritize Recall  
- Spam detection → prioritize Precision  

---

### 🔹 Multi-Class Classification (Softmax)
- One correct class  
- Probabilities sum to 1  
- Used when classes are mutually exclusive  

---

### 🔹 Multi-Label Classification
- Multiple labels possible  
- Uses Sigmoid activation  
- Each label is independent  

---

### 🔹 Hamming Loss
- Measures fraction of incorrect labels  

Formula:
Hamming Loss = Wrong Labels / Total Labels  

💡 Useful for multi-label problems

---

## 💼 Real-World Use Case (Fraud Detection)

1. Use stratified split  
2. Apply cross-validation  
3. Train model  
4. Tune threshold based on business needs  
5. Evaluate using appropriate metrics  

---

## 🧠 Key Takeaways

- Data splitting impacts model performance significantly  
- Stratification is critical for imbalanced datasets  
- Cross-validation improves robustness  
- Threshold tuning aligns model with business goals  
- Multi-class ≠ Multi-label  
- Hamming Loss is essential for multi-label evaluation  

---

## 📁 Project Structure

```
Day-20-Advanced-Classification/
│── Day20_Advanced_Classification.ipynb
│── solution.py
│── README.md
```

---

## 🚀 Next Steps

- Implement StratifiedKFold  
- Plot Precision-Recall Curve  
- Experiment with different thresholds  
- Try multi-label classification using real dataset  

---

## ✍️ Author
AI Learning Journey 🚀
