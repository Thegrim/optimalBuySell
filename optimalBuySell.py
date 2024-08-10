import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('/Users/lucas/Desktop/Olli/mock_qqq_data.csv', index_col='Date', parse_dates=True)

def find_optimal_buy_sell(prices):
    n = len(prices)
    if n < 2:
        return None, None
    
    # Initialize variables
    min_price = float('inf')
    max_profit = 0
    buy_date = sell_date = None
    
    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
            potential_buy_date = df.index[i]
        
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            buy_date = potential_buy_date
            sell_date = df.index[i]
    
    return buy_date, sell_date

# Find the optimal buy and sell dates
buy_date, sell_date = find_optimal_buy_sell(df['Close'].values)

if buy_date and sell_date:
    buy_price = df.loc[buy_date, 'Close']
    sell_price = df.loc[sell_date, 'Close']
    profit = sell_price - buy_price
    profit_percentage = (profit / buy_price) * 100
    
    print(f"Optimal buy date: {buy_date.date()}")
    print(f"Optimal buy price: ${buy_price:.2f}")
    print(f"Optimal sell date: {sell_date.date()}")
    print(f"Optimal sell price: ${sell_price:.2f}")
    print(f"Profit: ${profit:.2f}")
    print(f"Profit percentage: {profit_percentage:.2f}%")
else:
    print("No profitable trade found.")

# Visualize the data and the buy/sell points
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='QQQ Price')
plt.scatter(buy_date, buy_price, color='green', label='Buy Point', marker='^', s=100)
plt.scatter(sell_date, sell_price, color='red', label='Sell Point', marker='v', s=100)
plt.title('QQQ ETF Price with Optimal Buy and Sell Points')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('/Users/lucas/Desktop/Olli/qqq_buy_sell_points.png')
plt.close()

print(f"The chart has been saved as 'qqq_buy_sell_points.png' in the specified directory.")