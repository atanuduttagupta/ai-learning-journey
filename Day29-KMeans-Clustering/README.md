
# Day 29 — Clustering Basics + KMeans

---

# 🚀 Topics Covered

- Clustering Basics
- Unsupervised Learning
- Distance Metrics
- KMeans Clustering
- Centroid
- WCSS
- Elbow Method
- Silhouette Score
- Cluster Visualization
- Practical Business Use Cases
- Advantages & Limitations
- Interview Questions

---

# 📘 What is Clustering?

Clustering is an **Unsupervised Machine Learning** technique used to group similar data points together.

Unlike supervised learning, clustering does not require labeled data.

The model automatically discovers hidden patterns inside the dataset.

---

# 🎯 Goal of Clustering

The main objective is:

- Maximize similarity within clusters
- Minimize similarity between clusters

---

# 🧠 Real-World Intuition

Imagine a shopping mall dataset containing:

- Income
- Spending Score
- Purchase Frequency

Clustering can automatically discover:

- Premium Customers
- Budget Customers
- High-Spending Customers
- Occasional Buyers

---

# 📏 Distance Metrics

Clustering heavily depends on distance calculations.

## Euclidean Distance

Most common distance metric.

Formula:

d = √((x₂ - x₁)² + (y₂ - y₁)²)

---

# 🤖 KMeans Clustering

KMeans is a partition-based clustering algorithm.

It divides the dataset into:

# K Clusters

Each cluster contains a center called:

# 🎯 Centroid

---

# 🔄 Working of KMeans

## Step 1

Choose number of clusters (K)

---

## Step 2

Initialize random centroids

---

## Step 3

Assign points to nearest centroid

---

## Step 4

Update centroid positions

---

## Step 5

Repeat until centroids stabilize

---

# 🎯 Centroid

A centroid represents the average location of points inside a cluster.

Formula:

Centroid = (1/N) Σxᵢ

---

# 📉 WCSS (Within Cluster Sum of Squares)

KMeans minimizes:

# WCSS

WCSS measures cluster compactness.

Lower WCSS:

✅ Better clusters  
✅ Tighter grouping  

Higher WCSS:

❌ Poor clustering  
❌ Scattered data  

---

# 📊 Elbow Method

Used to determine optimal K.

## Process

1. Train KMeans for multiple K values
2. Compute WCSS
3. Plot K vs WCSS
4. Find elbow point

The elbow point is usually the best cluster count.

---

# 📈 Silhouette Score

Measures clustering quality.

## Score Range

| Score | Meaning |
|---|---|
| Near +1 | Excellent |
| Near 0 | Overlapping |
| Near -1 | Poor Clustering |

---

# 🏦 Practical Business Use Cases

| Industry | Use Case |
|---|---|
| Banking | Customer Segmentation |
| E-commerce | Product Recommendation |
| Telecom | Churn Detection |
| Healthcare | Patient Grouping |
| Cybersecurity | Threat Pattern Analysis |

---

# ✅ Advantages of KMeans

- Simple & Easy
- Fast on Large Datasets
- Scalable
- Effective for Segmentation
- Easy Visualization

---

# ❌ Limitations of KMeans

- Need to choose K manually
- Sensitive to outliers
- Assumes spherical clusters
- Poor for irregular shapes
- Initialization affects results

---

# 💡 Key Takeaways

✅ Clustering is unsupervised learning

✅ KMeans groups similar data points

✅ Centroids define cluster centers

✅ WCSS measures compactness

✅ Elbow Method helps choose K

✅ Silhouette Score evaluates quality

✅ KMeans is heavily used in BFSI and recommendation systems

---

# 🚀 Next Topic

Day 30:

- Dimensionality Reduction
- PCA
- Curse of Dimensionality
- Variance Explained
- Feature Compression

---
