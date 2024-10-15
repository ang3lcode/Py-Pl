to_do =  ["Dirigirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]

mix = ["string", 1, 2.5, True, [3, 4]]
# ¿Cómo se determina la longitud de una lista?
# Para saber cuántos elementos hay en una lista, se usa la función len:

print(len(mix))
# ¿Cómo se accede a elementos específicos de una lista?
# Se puede acceder a los elementos de una lista utilizando índices, donde el índice comienza en 0:

print(mix[0])  # Primer elemento
print(mix[-1])  # Último elemento
# ¿Cómo se realizan operaciones de slicing en listas?
# El slicing permite obtener sublistas a partir de una lista existente, especificando un rango de índices:

print(mix[1:3])  # Desde el índice 1 hasta el 2 (el 3 no se incluye)
print(mix[:2])  # Desde el inicio hasta el índice 1
print(mix[2:])  # Desde el índice 2 hasta el final
# ¿Qué métodos de manipulación de listas existen?
# Añadir elementos al final: append()

mix.append(False)
print(mix)
# Insertar elementos en una posición específica: insert()

mix.insert(1, ["A", "B"])
print(mix)
# Encontrar la primera aparición de un elemento: index()

print(mix.index(["A", "B"]))
# Encontrar el mayor y menor elemento: max() y min()

numbers = [1, 2, 3.5, 90, 100]
print(max(numbers))
print(min(numbers))
# ¿Cómo se eliminan elementos de una lista?
# Eliminar por índice: del

del numbers[-1]
print(numbers)
# Eliminar una porción de la lista:

del numbers[0:2]
print(numbers)
# Eliminar toda la lista:

del numbers