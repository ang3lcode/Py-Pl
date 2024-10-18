# factorial  numero
def factorial( n ):
    if n == 0:
        return 1
    else:
        return n * factorial( n - 1 )
factorial_5 = print( factorial( 5 ))

# fibonacci
def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la función
result = sum_numbers(5)
print(f"Suma de los primeros 5 números es: {result}")

#reto
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n - 1)

# Probar la función con varios valores
for i in range(11):
    print(f"Sumatoria de {i} es: {sumatoria(i)}")