# Day 03 - Semantic Search

## 🧠 Problem

Traditional search relies on exact word matching.

Example:
- Query: "couch"
- Text: "I bought a new sofa"

👉 No match ❌

---

## 🔹 Solution: Semantic Search

Instead of matching words, AI matches **meaning**.

Steps:
1. Convert text into vectors (numbers)
2. Compare similarity
3. Return closest match

---

## 📊 Example

```python
query = "I love AI"

documents = [
    "AI is amazing",
    "I enjoy machine learning",
    "The weather is nice"
]