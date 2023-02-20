import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from yellowbrick.cluster import KElbowVisualizer

# Cargar datos
compras = pd.read_csv('compras.csv')

# Seleccionar variables de interés
X = compras[['Val_compras', 'Num_compras', 'Categorias']]

# Transformar la variable categórica a numérica con one-hot encoding
X = pd.get_dummies(X)

# Normalizar datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reducir dimensionalidad con PCA
pca = PCA()
pipeline = make_pipeline(scaler, pca)
pipeline.fit(X_scaled)
explained_variances = pca.explained_variance_ratio_
plt.plot(np.cumsum(explained_variances))
plt.xlabel('Número de componentes')
plt.ylabel('Varianza explicada acumulada')
plt.show()

# Elegir número de componentes
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Encontrar número óptimo de clusters con el método del codo
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(X_pca)
visualizer.show()

# Entrenar modelo con número óptimo de clusters
k = visualizer.elbow_value_
model = KMeans(n_clusters=k)
model.fit(X_pca)

# Graficar resultados
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=model.labels_, cmap='Set1')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()