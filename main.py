import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import seaborn as sns

cov_matrix = np.array([[11., -9.8], [-9.8, 11.]])

def profit_next_year_mc(mean_inflation, mean_volume, n):
    profits = []
    for i in range(n):
        rate_sales_volume = multivariate_normal.rvs(mean=[mean_inflation, mean_volume], cov=cov_matrix, size=1000)
        price = 100 * (100 + rate_sales_volume[:, 0]) / 100
        volume = rate_sales_volume[:, 1]
        loan_and_cost = 50 * volume + 45 * (100 + 3 * rate_sales_volume[:, 0]) * (volume / 100)
        profit = np.mean(price * volume - loan_and_cost)
        profits.append(profit)
    return profits

mean_inflation_percentages = [0, 2, 5, 10]
sales_values = [500, 800, 1000]
times = 100

simulation_results = {}

for inflation in mean_inflation_percentages:
    for volume in sales_values:
        simulation_results[(inflation, volume)] = profit_next_year_mc(inflation, volume, times)

inflation_values, volume_values, average_profits = [], [], []
for (inflation, volume), profits in simulation_results.items():
    inflation_values.extend([inflation] * times)
    volume_values.extend([volume] * times)
    average_profits.extend(profits)

plt.figure(figsize=(12, 8))
sns.scatterplot(x=inflation_values, y=volume_values, size=average_profits, legend=False, sizes=(20, 200))
plt.xlabel('Mean Inflation Percentages')
plt.ylabel('Sales Volume')
plt.title('Profit')
plt.grid(True)
plt.show()
