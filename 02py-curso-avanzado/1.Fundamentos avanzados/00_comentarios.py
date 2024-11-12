#Comentarios y Docstrings en Python
def calcular_average(numbers):
   """
   Calcula el promedio de una lista.

   parametros: 
   numbers (list): una lista de números enteros o flotantes 

   retorna:
   float: El promedio de los numeros en la lista
   """
   return sum(numbers) / len(numbers)

#imprimiendo el resultado
print(calcular_average([1,2,3,4,5]))