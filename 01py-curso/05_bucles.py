# for 
numbers = [1, 2, 3, 4, 5, 6, ]
for i in numbers:
    if i == 3:
        continue
    print("Aqui i es igual a: ", i **2)

for i in range(2, 11): # inicio de 0 al 10  pero puedo especificar  en donde inicia
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruta in fruits:
    print(fruta)
    if fruta == 'Naranja':
        print("Naranja encontrada")

# while 
x = 0
while x < 5 :
    if x == 3:
        break
    print(x)
    x += 1