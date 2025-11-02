import pandas as pd
import numpy as np

data = {'Age': [25, np.nan, 30, np.nan, 40],
        'City': ['Delhi', 'Mumbai', np.nan, 'Kolkata', 'Delhi']}
df = pd.DataFrame(data)
print("Before Imputation:\n", df)

mean_val = np.nanmean(df['Age'])
df['Age'] = [mean_val if np.isnan(x) else x for x in df['Age']] 
mode_val = df['City'].mode()[0]
df['City'] = [mode_val if pd.isna(x) else x for x in df['City']]

print("\nAfter Imputation:\n", df)
