import json
file_path ='01py-curso/R_W_archivos/json/products.json'

#Lectura del archivo
with open(file_path, mode='r') as file:
    products = json.load(file)

#Mostrar el contenido
for product in products:
    #print(product)
    print(f"Product: {product['name']}, Price: {product['price']}")