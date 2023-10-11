import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

x = np.random.rand(3100)
y = 2 * x + 1 + np.random.rand(3100)

data = pd.DataFrame({'x': x, 'y': y})

data.to_excel('data.xlsx', index=False)

plt.scatter(x, y, label='Дані')
plt.xlabel('Ознака x')
plt.ylabel('Ознака y')
plt.legend()
plt.title('Дані і лінійна регресія')

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Модель лінійної регресії: y = {slope:.2f}x + {intercept:.2f}")
print(f"Коефіцієнт кореляції (r-value): {r_value:.2f}")
print(f"P-значення: {p_value:.2f}")

line = slope * x + intercept
plt.plot(x, line, color='red', label='Лінія регресії')
plt.legend()

plt.show()