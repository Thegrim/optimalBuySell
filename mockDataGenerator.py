import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set a random seed for reproducibility
np.random.seed(42)

# Generate dates for the past 365 days
end_date = datetime.now().date()
start_date = end_date - timedelta(days=364)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate mock closing prices
initial_price = 300  # Starting price
daily_returns = np.random.normal(loc=0.0005, scale=0.02, size=365)  # Daily return with slight upward bias
prices = initial_price * (1 + daily_returns).cumprod()

# Create the dataframe
df = pd.DataFrame({
    'Date': date_range,
    'Close': prices
})

# Set the index to Date
df.set_index('Date', inplace=True)

# Round the closing prices to two decimal places
df['Close'] = df['Close'].round(2)

# Display the first few rows
print(df.head())

# Display basic statistics
print(df.describe())

# Optional: Save to CSV
# save to path /yourPath



df.to_csv('/yourPath.csv')
