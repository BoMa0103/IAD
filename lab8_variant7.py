import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

n = 80
c = 4

data = pd.DataFrame({
    'Feature 1': np.random.rand(n),
    'Feature 2': np.random.rand(n),
    'Class': np.random.randint(1, c + 1, size=n)
})

kmeans = KMeans(n_clusters=c)
data['Cluster'] = kmeans.fit_predict(data[['Feature 1', 'Feature 2']])

for cluster in range(1, c + 1):
    plt.scatter(data[data['Class'] == cluster]['Feature 1'],
                data[data['Class'] == cluster]['Feature 2'],
                label=f'Class {cluster}')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Розбиття об\'єктів спостереження відповідно до класів')
plt.legend()

plt.figure()
plt.scatter(data['Feature 1'], data['Feature 2'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Результати кластеризації даних')

plt.figure()
linked = linkage(data[['Feature 1', 'Feature 2']], 'ward')
dendrogram(linked, orientation='top', labels=data['Class'].values)
plt.title('Дендрограма кластеризації')
plt.xlabel('Об\'єкти спостереження')
plt.ylabel('Відстань')

plt.show()