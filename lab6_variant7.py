import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

np.random.seed(0)
n = 100
mean = [1, 0]
cov_matrix = [[10, 1], [1, 1]]
data = np.random.multivariate_normal(mean, cov_matrix, n)

x = data[:, 0]
y = data[:, 1]

plt.scatter(x, y, label='Дані')
plt.xlabel('Ознака x')
plt.ylabel('Ознака y')
plt.legend()
plt.title('Дані')

correlation_coefficient, p_value = pearsonr(x, y)

print(f"Коефіцієнт кореляції Пірсона: {correlation_coefficient}")
print(f"p-значення: {p_value}")

plt.figure()
plt.scatter(x, y, label='Дані')
plt.xlabel('Ознака x')
plt.ylabel('Ознака y')
plt.legend()
plt.title(f'Кореляція (r={correlation_coefficient:.2f})')

alpha = 0.05

if p_value < alpha:
    print("За рівнем значущості 0.05 гіпотезу про некорельованість ознак відхиляють")
else:
    print("На рівні значущості 0.05 немає достатніх доказів відхилення гіпотези про некорельованість ознак")

plt.show()