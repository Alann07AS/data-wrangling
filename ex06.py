import pandas as pd
import numpy as np

business_dates = pd.bdate_range('2021-01-01', '2021-12-31')

#generate tickers
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

#create indexs
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])
# create DFs
market_data = pd.DataFrame(index=index,
                        data=np.random.randn(len(index), 1),
                        columns=['Prediction'])
print(market_data)

# Unstack the DataFrame
unstacked_data = market_data.unstack(level='Ticker')

# Display the first 3 rows of the unstacked DataFrame
print(unstacked_data.head(3))

import matplotlib.pyplot as plt
# Plot the 5 time series in the same plot
unstacked_data.plot(title='Daily Predictions for Companies (Tickers)', figsize=(10, 6))
plt.xlabel('Date')
plt.ylabel('Prediction')
plt.show()
