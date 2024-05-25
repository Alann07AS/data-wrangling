import pandas as pd
import numpy as np

#generate days
all_dates = pd.date_range('2021-01-01', '2021-12-15')
business_dates = pd.bdate_range('2021-01-01', '2021-12-31')

#generate tickers
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

# Create indexes
index_alt = pd.MultiIndex.from_product([all_dates, tickers], names=['Date', 'Ticker'])
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])

# Create DataFrames
market_data = pd.DataFrame(index=index,
                            data=np.random.randn(len(index), 3),
                            columns=['Open', 'Close', 'Close_Adjusted'])
print(market_data)
alternative_data = pd.DataFrame(index=index_alt,
                                data=np.random.randn(len(index_alt), 2),
                                columns=['Twitter', 'Reddit'])

# Merge DataFrames on MultiIndex
merged_data = pd.merge(market_data, alternative_data, how='left', left_index=True, right_index=True)

# Fill missing values with 0
merged_data.fillna(0, inplace=True)

# Display the merged DataFrame
print(merged_data)
