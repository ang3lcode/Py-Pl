class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 25)

persona1.greet()
persona2.greet()