# Day 30 — Hierarchical Clustering

## 📌 Topics Covered

- Hierarchical Clustering
- Dendrogram
- Agglomerative Clustering
- Divisive Clustering
- Single Linkage
- Complete Linkage
- Average Linkage
- Ward Linkage
- Distance Metrics
- Practical Applications
- Advantages & Limitations
- Hierarchical Clustering vs KMeans

---

# 🌳 What is Hierarchical Clustering?

Hierarchical Clustering is an **unsupervised machine learning algorithm** that groups similar data points into clusters.

Unlike KMeans:
- No need to predefine K
- Creates hierarchical cluster relationships
- Uses dendrogram visualization

Two approaches:
- Agglomerative → merge clusters
- Divisive → split clusters

---

# 🌳 Dendrogram

A dendrogram is a tree-like structure showing:
- cluster merging
- cluster similarity
- hierarchical relationships

## Important Interpretation

- Bottom nodes → data points
- Vertical lines → cluster merging
- Height → cluster distance

Higher merge height:
- lower similarity

Lower merge height:
- higher similarity

---

# 📌 Types of Hierarchical Clustering

| Type | Description |
|---|---|
| Agglomerative | Bottom-up merging |
| Divisive | Top-down splitting |

---

# 1️⃣ Agglomerative Clustering

## Workflow

1. Each point becomes its own cluster
2. Compute distances
3. Merge nearest clusters
4. Recompute distances
5. Repeat

## Industry Usage

✅ Most commonly used hierarchical clustering method

---

# 2️⃣ Divisive Clustering

## Workflow

1. Start with one cluster
2. Split least similar groups
3. Repeat recursively

## Important

❌ Computationally expensive  
❌ Rarely used in production

---

# 🔗 Linkage Methods

Linkage methods define:
> “How cluster distance is calculated.”

---

# 📌 Single Linkage

Uses minimum distance between clusters.

## Advantages
- Detects irregular shapes
- Good for connected data

## Limitations
- Chaining effect
- Sensitive to noise

---

# 📌 Complete Linkage

Uses maximum distance between clusters.

## Advantages
- Compact clusters
- Less chaining

## Limitations
- Sensitive to outliers

---

# 📌 Average Linkage

Uses average pairwise distance.

## Advantages
- Balanced clustering
- Stable results

## Limitations
- Computationally expensive

---

# 📌 Ward Linkage

Minimizes cluster variance.

Very similar philosophy to KMeans.

## Advantages
- Compact clusters
- Industry favorite

## Limitations
- Sensitive to outliers
- Prefers spherical clusters

---

# 📏 Distance Metrics

| Metric | Usage |
|---|---|
| Euclidean | Most common |
| Manhattan | Grid distance |
| Cosine | Text similarity |
| Minkowski | Generalized metric |

---

# 🧮 Euclidean Distance Formula

```math
d = √((x₂ - x₁)² + (y₂ - y₁)²)
```

---

# 💻 Dendrogram Python Code

```python
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Generate sample data
X, y = make_blobs(
    n_samples=30,
    centers=4,
    random_state=42
)

# Create linkage matrix
linked = linkage(X, method='ward')

# Plot dendrogram
plt.figure(figsize=(14,6))

dendrogram(
    linked,
    leaf_rotation=90,
    leaf_font_size=10
)

plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.show()
```

---

# 🏢 Practical Applications

## 🛒 Customer Segmentation
- spending behavior
- purchase analysis

## 🧬 Bioinformatics
- DNA clustering
- gene analysis

## 📄 Document Clustering
- news grouping
- legal document analysis

## 🏥 Medical Diagnosis
- symptom grouping
- patient similarity

---

# ✅ Advantages

- No need to predefine K
- Dendrogram visualization
- Flexible distance metrics
- Detects nested relationships
- Highly interpretable

---

# ❌ Limitations

- Slow for large datasets
- Memory intensive
- Sensitive to outliers
- Greedy process
- Poor scalability

---

# 🔥 Hierarchical Clustering vs KMeans

| Feature | Hierarchical | KMeans |
|---|---|---|
| Type | Tree-based | Centroid-based |
| Need K Initially | No | Yes |
| Speed | Slow | Fast |
| Scalability | Weak | Strong |
| Interpretability | High | Medium |
| Large Dataset Support | Poor | Excellent |

---

# 🧠 Interview Questions

## Why use dendrogram?
To visually determine optimal clusters.

## Why is Ward linkage popular?
Because it minimizes variance and creates compact clusters.

## Why is hierarchical clustering expensive?
Because pairwise distances are repeatedly computed.

---

# 🚀 Key Takeaways

✅ Hierarchical clustering builds cluster hierarchy.

✅ Dendrogram visualizes merging patterns.

✅ Agglomerative clustering is most popular.

✅ Ward linkage often produces best compact clusters.

✅ Better interpretability than KMeans.

✅ Poor scalability for massive datasets.

---

# 📚 End of Day 30
