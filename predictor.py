import numpy as np
import pandas as pd

np.random.seed(42)

stocks = ["Apple", "Google", "Amazon", "Microsoft", "Tesla"]

num_stocks = len(stocks)  
num_days = 30              
initial_prices = np.random.randint(100, 500, size=num_stocks)
daily_changes = np.random.uniform(-0.05, 0.05, size=(num_days, num_stocks))
prices = np.zeros((num_days, num_stocks))
prices[0] = initial_prices

for day in range(1, num_days):
    prices[day] = prices[day-1] * (1 + daily_changes[day])

df = pd.DataFrame(prices, columns=stocks)
df.index.name = "Day"
print(df.head())

returns = df.pct_change().fillna(0)
print(returns.head())

total_returns=(df.iloc[-1]-df.iloc[0])/df.iloc[0]*100
print(total_returns.head())

best_stock = total_returns.idxmax()
worst_stock = total_returns.idxmin()
print("Best stock:", best_stock)
print("Worst stock:", worst_stock)
