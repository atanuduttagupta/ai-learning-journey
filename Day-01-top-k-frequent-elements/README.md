# Day 01 - Top K Frequent Elements

## 🧠 Problem

Find the **K most frequent elements** from a list.

Example:

words = ["ai", "ml", "ai", "data", "ml", "ai", "data", "ml", "data", "data"]  
k = 2  

Output:  
['data', 'ai']

---

## 🔹 Approaches

### 1. Traditional (Sorting)
- Count frequency using a dictionary  
- Sort all elements  
- Pick top K  

⏱ Time Complexity: O(n log n)

---

### 2. Pythonic (Counter)
- Use `collections.Counter`  
- Get top K using `most_common(k)`  

⏱ Time Complexity: O(n log k)

---

## 💡 Key Learning

Simple patterns like frequency counting are widely used in:
- NLP (word frequency)
- Feature engineering
- Recommendation systems

---

## 📌 Files

- `notebook.ipynb` → Step-by-step learning   
