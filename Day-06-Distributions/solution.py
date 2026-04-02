import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# ============================================================
# 🚀 Step 1: Define average traffic (λ)
# ============================================================
# Average clicks per minute
lambda_val = 5

# ============================================================
# 📊 Step 2: Simulate traffic
# ============================================================
# Simulate 1000 minutes of traffic
samples = np.random.poisson(lam=lambda_val, size=1000)

# Print average
print("Average clicks per minute:", np.mean(samples))

# ============================================================
# 📈 Step 3: Visualize distribution
# ============================================================
plt.hist(samples, bins=15)
plt.title("Clicks Per Minute (Poisson Distribution)")
plt.xlabel("Clicks per minute")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# 🔥 Step 4: Compare different traffic rates (optional)
# ============================================================
for lam in [2, 5, 10]:
    samples = np.random.poisson(lam=lam, size=1000)
    plt.hist(samples, bins=15, alpha=0.5, label=f"λ={lam}")

plt.legend()
plt.title("Traffic Comparison for Different Rates")
plt.xlabel("Clicks per minute")
plt.ylabel("Frequency")
plt.show()