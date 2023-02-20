from faker import Faker
import csv

# Crear una instancia de Faker
fake = Faker()

# Generar datos ficticios de clientes con identificadores únicos
clientes = []
for _ in range(3000):
    id_unico = fake.uuid4()
    edad = fake.random_int(min=18, max=70)
    sexo = fake.random_element(elements=('M', 'F'))
    clientes.append({"id": id_unico, "edad": edad, "sexo": sexo})

# Crear un archivo CSV
with open('clientes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Edad", "Sexo"])
    for cliente in clientes:
        writer.writerow([cliente["id"], cliente["edad"], cliente["sexo"]])