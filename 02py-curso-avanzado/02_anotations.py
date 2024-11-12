# IDs de empleados
id1:int = 101
id2:int = 102

# sumar los IDs
tatal_id: int = id1 + id2

# Mostrar resultado
print( tatal_id )

# ejemplo 2
def add_employee_ids( id1: int, id2: int ) -> int:
   return id1 + id2

print(add_employee_ids(201, 202))

# ejemplo 3 class
class employee:
    name: str 
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float ):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce( self )-> str:
        return f'Hola me llamo {self.name}, tengo {self.age}'

employee = employee( 'carlos', 30, 3500.00 )
print(employee.introduce())

