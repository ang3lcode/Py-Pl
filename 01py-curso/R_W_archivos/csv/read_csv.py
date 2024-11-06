import csv

#leer un archivo
"""with open('01py-curso/R_W_archivos/csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar la información por columnas
with open('01py-curso/R_W_archivos/csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")