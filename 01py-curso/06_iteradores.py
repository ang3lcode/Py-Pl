# iterador
# crear lista
my_list = [1,2,3,4]
# ontener el iterador
my_iter = iter(my_list)

# usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) # ya no puedo iterar otro por que la liosta solo tiene 4

# Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

#Iterar en la cadena por bucles
for char in iter_text:  
    print(char)


    # Crear un iterador para los numeros impares
#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1, limit+1, 2)) # tercer numero son los saltos

#Usar el iterador
for num in odd_itter:
    print(num)


def my_generator():
    yield 1 #cuando se invoca  me genera valores diferentes
    yield 2
    yield 3

for value in my_generator():
    print(value) 

# fibonacci
# 0 1 1 2 3 5 8 13 21 ...

def fibonacci(limit):
    a, b = 0, 1
    while  a < limit:
        yield a
        a, b = b, a+b
for num in fibonacci(10):
    print(num)