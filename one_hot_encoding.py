import pandas as pd
import numpy as np


data = {'Color': ['Red', 'Blue', 'Green', 'Red']}
df = pd.DataFrame(data)

unique_vals = df['Color'].unique()

one_hot = pd.DataFrame()

for val in unique_vals:
    one_hot[val] = [1 if x == val else 0 for x in df['Color']]

final_df = pd.concat([df, one_hot], axis=1)
print(final_df)
