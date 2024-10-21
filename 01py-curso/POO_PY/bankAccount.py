class BankAccount:
    def __init__(self, account_holder, balance) :
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"se ha depositado {amount}, saldo actual {self.balance}")
        else:
            print("no se puede depositar")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"se retiro {amount}. saldo actual {self.balance}")

    def deactivate(self):
        self.is_active = False
        print(f"la cuenta fue desactivada")

    def activate(self):
        self.is_active = True
        print("La cuenta ha sido activada")


# Crear objetos de la clase BankAccount
cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactivate()
cuenta1.deposit(200)
cuenta1.activate()
cuenta1.deposit(200)