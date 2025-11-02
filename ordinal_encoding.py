import pandas as pd
import numpy as np

data = {'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']}
df = pd.DataFrame(data)
size_order = ['Small', 'Medium', 'Large']


encoded = []
for val in df['Size']:
    encoded.append(size_order.index(val))

df['Size_Encoded'] = encoded
print(df)
