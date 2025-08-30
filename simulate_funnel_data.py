import pandas as pd
import numpy as np
import requests

# Step 1: Load campaign data from API
url = 'https://marketing-api-1-ldfh.onrender.com/api/campaigns'
response = requests.get(url)
data = response.json()

# Step 2: Flatten JSON into a DataFrame
df = pd.json_normalize(data)

# Step 3: Simulate funnel metrics
np.random.seed(42)  # For reproducibility
df['impressions'] = np.random.randint(10000, 50000, df.shape[0])
df['clicks'] = (df['impressions'] * np.random.uniform(0.05, 0.2, df.shape[0])).astype(int)
df['leads'] = (df['clicks'] * np.random.uniform(0.2, 0.5, df.shape[0])).astype(int)
df['conversions'] = (df['leads'] * (df['conversion_rate'] / 100)).astype(int)

# Step 4: Save to CSV
df.to_csv('campaign_with_funnel_data.csv', index=False)
print("✅ Data saved as 'campaign_with_funnel_data.csv'")