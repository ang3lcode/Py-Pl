# diccionario  necesita clave valor
numbers = {1:"uno", 2:"dos", 3:"tres"} 
print(numbers[2]) #obtengo "dos"

information = {"nombre": "jago",
               "Apellido": "ave",
               "Altura": 1.70,
               "Edad": 29}
print(information)

del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = {"Carla": {"Apellido": "a",
               "Altura": 2,
               "Edad": 29},
                "Diego": {"Apellido": "b",
               "Altura": 3,
               "Edad": 32}}
print(contacts["Carla"])