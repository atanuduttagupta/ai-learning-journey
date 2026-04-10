import numpy as np
import pandas as pd

np.random.seed(42)

# Generate data
amount = np.random.normal(500, 50, 1000)
amount = np.append(amount, [1200, 1500, 50])

df = pd.DataFrame({"amount": amount})

# IQR
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

iqr_outliers = df[(df['amount'] < lower) | (df['amount'] > upper)]

# Z-score
mean = df['amount'].mean()
std = df['amount'].std()

df['z_score'] = (df['amount'] - mean) / std
z_outliers = df[np.abs(df['z_score']) > 3]

print("IQR Outliers:")
print(iqr_outliers)

print("\nZ-score Outliers:")
print(z_outliers)
