import pandas as pd
import numpy as np

# Cargar los archivos CSV con los datos de clientes y productos
df_clientes = pd.read_csv('clientes.csv')
df_productos = pd.read_csv('productos_seleccionados.csv')

# Definir el número máximo y mínimo de compras que se generarán para cada cliente
num_compras_min = 1
num_compras_max = 104

# Inicializar una lista para almacenar las compras
compras = []

# Generar compras aleatorias para cada cliente
for i, row in df_clientes.iterrows():
    num_compras = np.random.randint(num_compras_min, num_compras_max + 1)
    val_compras = 0
    categorias = []
    for j in range(num_compras):
        # Seleccionar productos aleatorios del catálogo de productos
        producto = df_productos.sample().iloc[0]
        
        # Eliminar todos los caracteres no numéricos del precio del producto
        precio_limpio = ''.join(filter(str.isdigit, producto['Precio']))

        # Convertir el precio a un número entero y sumarlo al valor total de las compras
        val_compras += int(precio_limpio)
        
        # Agregar la categoría del producto a la lista de categorías
        categorias.append(producto['Categoria'])
        
    # Agregar una nueva fila al DataFrame de compras
    compras.append({
        'ID_Cliente': row['ID'],
        'Val_compras': val_compras,
        'Num_compras': num_compras,
        'Categorias': ','.join(categorias)
    })

# Crear un DataFrame a partir de la lista de compras
df_compras = pd.DataFrame(compras)

# Guardar el DataFrame en un nuevo archivo CSV
df_compras.to_csv('compras.csv', index=False)