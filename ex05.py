import pandas as pd

# Create the DataFrame
data = {'value': [20.45, 22.89, 32.12, 111.22, 33.22, 100, 99.99],
        'product': ['table', 'chair', 'chair', 'mobile phone', 'table', 'mobile phone', 'table']}
df = pd.DataFrame(data)

# Compute min, max, and mean price for each product in one line
result = df.groupby('product')['value'].agg(['min', 'max', 'mean'])

# Display the result
print(result)
