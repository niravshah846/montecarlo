import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
simulations=10000
years=30
initial_investment=10000
annual_withdrawal=6000
expected_return=0.08
volatility=0.15

# generate the simulation
market_results=np.random.normal(expected_return, volatility, (years, simulations))
portfolio_paths=pd.DataFrame(index=range(years), columns=range(simulations))
portfolio_paths.iloc[0]=initial_investment
for t in range(1,years):
# previous balance * (1 + current year return)-annual withdrawal
   prev_balance=portfolio_paths.iloc[t-1]
   current_returns=market_results[t]

# formula= (balance*return)-withdrawal
   new_balance=prev_balance * (1+current_returns)-annual_withdrawal
   portfolio_paths.iloc[t]= np.maximum(0, new_balance)

#visualization with matplotlib
plt.figure(figsize=(12,6))
plt.plot(portfolio_paths, color='gray', alpha=0.1)
plt.plot(portfolio_paths.median(axis=1), color='blue', linewidth=3, label='Median Path')
plt.plot(portfolio_paths.quantile(0.95, axis=1), color='green', linestyle='--', label='Best case scenario')
plt.plot(portfolio_paths.quantile(0.05, axis=1), color='red', linestyle='--', label='Worst case scenario')
plt.title('Monte Carlo Simulation of Retirement Portfolio')
plt.xlabel('Years of retirement')
plt.ylabel('Portfolio Value')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 5. Success Rate Calculation
success_rate = (portfolio_paths.iloc[-1] > 0).mean() * 100
print(f"Probability of retirement success: {success_rate:.2f}%")
