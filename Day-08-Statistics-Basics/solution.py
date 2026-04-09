import numpy as np
import matplotlib.pyplot as plt

# Simulated session data
session_times = np.array([5, 6, 4, 3, 7, 8, 120])
print('Session Times:', session_times)

mean_val = np.mean(session_times)
median_val = np.median(session_times)
std_val = np.std(session_times)

print('\nStatistics:')
print('Mean:', mean_val)
print('Median:', median_val)
print('Std Dev:', std_val)

threshold = 2 * std_val
outliers = session_times[np.abs(session_times - mean_val) > threshold]
print('\nOutliers:', outliers)

# Visualization
plt.hist(session_times, bins=5)
plt.title('User Session Time Distribution')
plt.xlabel('Session Time (minutes)')
plt.ylabel('Frequency')
plt.show()