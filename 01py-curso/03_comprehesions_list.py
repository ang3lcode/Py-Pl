# list comprehesions
squares = [x**2 for x in range(1,11)]  #
print("Cuadrados: ", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [ ( temp * 9/5 )  + 32 for temp in celsius ]
print( "temperatura: ", fahrenheit)

# numeros pares
event = [ x for x in range(1, 21) if x%2 == 0]
print("numeeros pares: ", event)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [ [row[i] for row in matrix ]  for i in range( len(matrix[0] ) ) ]
print(matrix)
print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# Resultado:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 0
# []
# [1]
# [1, 4]
# [1, 4, 7]
# 1
# []
# [2]
# [2, 5]
# [2, 5, 8]
# 2
# []
# [3]
# [3, 6]
# [3, 6, 9]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]