# Day 32 — Naive Bayes, Probability Foundations & Gaussian Mixture Models (GMM)

## Topics Covered

- Probability vs Likelihood vs Odds vs Prior Probability
- Bayes Theorem
- Bernoulli Naive Bayes
- Multinomial Naive Bayes
- Gaussian Mixture Model (GMM)
- GMM vs KMeans
- Naive Bayes vs PCA
- Practical Use Cases
- Advantages & Limitations
- Tasks + Mini Projects

---

# Why This Topic Matters

Probability-based Machine Learning models power many real-world AI systems:

- Spam Detection
- Fraud Detection
- Credit Risk Analysis
- Sentiment Analysis
- Recommendation Systems
- Customer Segmentation

This notebook builds strong intuition behind probabilistic AI and statistical machine learning.

---

# Probability Foundations

## Probability
Measures the chance of an event occurring.

Example:
- Probability of rain = 0.8
- Probability of spam email = 0.95

---

## Likelihood
Measures how likely observed data fits a model.

Example:
- Likelihood of email words given spam class.

---

## Odds
Ratio of success probability to failure probability.

Example:
- Probability = 0.8
- Odds = 0.8 / 0.2 = 4

Meaning:
4 successful outcomes for every 1 failure.

---

## Prior Probability
Initial belief before observing evidence.

Example:
- 30% emails are spam
- Prior probability of spam = 0.3

---

# Bayes Theorem

Bayes theorem updates probability after observing evidence.

Formula:

P(A|B) = (P(B|A) × P(A)) / P(B)

Where:

| Term | Meaning |
|---|---|
| P(A|B) | Posterior Probability |
| P(B|A) | Likelihood |
| P(A) | Prior Probability |
| P(B) | Evidence |

---

# Naive Bayes

Naive Bayes is a probabilistic classification algorithm based on Bayes Theorem.

It assumes:
“All features are independent.”

This is called the:
## Naive Assumption

---

# Bernoulli Naive Bayes

Used when features are binary.

Examples:
- Yes / No
- 0 / 1
- Word Present / Not Present

## Common Applications
- Spam detection
- Binary text classification

### Advantages
- Fast
- Simple
- Works well on binary features

### Limitations
- Ignores frequency information
- Less effective on long documents

---

# Multinomial Naive Bayes

Used for count-based features.

Example:

| Word | Count |
|---|---|
| Free | 4 |
| Offer | 2 |
| Win | 5 |

## Common Applications
- NLP
- Sentiment Analysis
- News Classification
- Spam Filtering

### Advantages
- Excellent for NLP
- Handles sparse text data well
- Fast training

### Limitations
- Independence assumption unrealistic
- Struggles with correlated features

---

# Gaussian Mixture Model (GMM)

GMM is a probabilistic clustering algorithm.

Unlike KMeans:
- KMeans → Hard clustering
- GMM → Soft clustering

---

# Soft Clustering

Example:

| Customer | Cluster A | Cluster B |
|---|---|---|
| User 1 | 80% | 20% |

Meaning:
A data point can partially belong to multiple clusters.

---

# Why GMM is Powerful

GMM handles:
- Overlapping clusters
- Elliptical cluster shapes
- Uncertainty in data

better than KMeans.

---

# GMM vs KMeans vs PCA

| Feature | GMM | KMeans | PCA |
|---|---|---|---|
| Type | Probabilistic clustering | Distance clustering | Dimensionality reduction |
| Membership | Soft | Hard | No clusters |
| Main Goal | Model distributions | Group data | Reduce dimensions |
| Output | Probability clusters | Fixed clusters | Principal components |

---

# Naive Bayes vs PCA

| Naive Bayes | PCA |
|---|---|
| Classification algorithm | Dimensionality reduction |
| Predicts labels | Compresses features |
| Uses probability | Uses variance |
| Solves prediction problems | Solves feature reduction problems |

---

# Practical BFSI Applications

## Naive Bayes
- Fraud detection
- Email phishing detection
- Credit risk prediction

## GMM
- Customer segmentation
- Risk modeling
- Anomaly detection

## PCA + GMM Pipeline
1. PCA → Reduce dimensions
2. GMM → Cluster customers
3. Naive Bayes → Predict customer category

---

# Tasks Included

## Beginner
- Bernoulli Naive Bayes implementation
- Multinomial Naive Bayes comparison
- GMM clustering visualization

## Intermediate
- PCA before GMM
- Sentiment classification project

## Advanced
- Fraud detection pipeline
- Customer segmentation system

---

# Mini Project

## AI Spam Detection System

Build a spam detection pipeline using:
- Text preprocessing
- CountVectorizer
- Multinomial Naive Bayes
- Accuracy evaluation

---

# Final Takeaways

## Naive Bayes
- Fast probabilistic classifier
- Excellent for NLP and spam detection

## GMM
- Flexible probabilistic clustering model
- Handles uncertainty better than KMeans

## PCA
- Reduces dimensions
- Speeds up ML pipelines

---

# Industry Insight

Modern AI systems often combine:

PCA + GMM + Naive Bayes

to build scalable intelligent systems for:
- BFSI
- NLP
- Recommendation Engines
- Fraud Analytics
