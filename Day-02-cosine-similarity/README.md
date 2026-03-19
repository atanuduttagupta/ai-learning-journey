\# Day 02 - Cosine Similarity



\## 🧠 Overview



Cosine similarity is widely used in AI systems such as:

\- Semantic search

\- Recommendation systems

\- NLP embeddings

\- RAG (Retrieval Augmented Generation)



It helps measure how similar two vectors are based on their \*\*direction\*\*.



\---



\## 📌 Problem



How do we measure similarity between two vectors?



Instead of comparing values directly, cosine similarity measures the \*\*angle between vectors\*\*:



\- Smaller angle → more similar  

\- Larger angle → less similar 



\## 📏 Range of Cosine Similarity



Cosine similarity ranges from \*\*-1 to 1\*\*:



| Value | Interpretation |

|------|---------------|

| \*\*1\*\* | Vectors are identical (same direction) |

| \*\*0\*\* | No similarity (orthogonal/perpendicular) |

| \*\*-1\*\* | Vectors are completely opposite | 



\## 📌 Simple summary

\---



\## 📊 Example



```python

v1 = \[1, 2, 3]

v2 = \[5, -1, 7]

