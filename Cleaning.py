import pandas as pd
import uuid

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('productos.csv')

# Agregar una nueva columna con un ID único para cada fila
df['ID_Prod'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Seleccionar solo las columnas que se quieren mostrar
df2 = df[['ID_Prod', 'Precio', 'Categoria']]

# Guardar el nuevo DataFrame en un archivo CSV
df2.to_csv('productos_seleccionados.csv', index=False)