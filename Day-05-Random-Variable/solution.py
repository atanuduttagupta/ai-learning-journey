import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Different user types with different click behavior
segments = {    "casual_users": {0: 0.7, 1: 0.2, 2: 0.1},   
                "regular_users": {0: 0.4, 1: 0.4, 2: 0.2},    
                "power_users": {0: 0.2, 1: 0.5, 2: 0.3}}


simulation_results = {}
for segment, pmf in segments.items():    
    values = list(pmf.keys())    
    probs = list(pmf.values())    
    simulated = np.random.choice(values, size=1000, p=probs)    
    simulation_results[segment] = simulated
print(simulation_results.keys())

expected_clicks = {}
for segment, data in simulation_results.items():    
    expected_clicks[segment] = np.mean(data)
print(expected_clicks)

df = pd.DataFrame({"segment": list(expected_clicks.keys()),    
                   "avg_clicks": list(expected_clicks.values())})
df

plt.bar(df['segment'], df['avg_clicks'])
plt.xlabel('User Segment')
plt.ylabel('Average Clicks (CTR)')
plt.title('CTR Comparison Across User Segments')
plt.show()


