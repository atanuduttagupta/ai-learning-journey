import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Dataset
df = pd.DataFrame({
    "age": [25, 45, 35, 50, 23, 40],
    "salary": [20000, 50000, 30000, 60000, 22000, 52000],
    "churn": [0, 1, 0, 1, 0, 1]
})

X = df[["age", "salary"]]
y = df["churn"]

# 🔹 Step 1: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Step 2: Scaling (FIT ONLY ON TRAIN DATA)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 🔹 Step 3: Model Training
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 🔹 Step 4: Prediction
pred = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, pred))

probs = model.predict_proba(X_test_scaled)[:, 1]

plt.scatter(range(len(probs)), probs)
plt.axhline(y=0.5, linestyle='--')

plt.title("Predicted Probabilities")
plt.xlabel("Sample Index")
plt.ylabel("Probability of Class 1")

plt.show()
