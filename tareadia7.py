class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("No tiene suficiente saldo en su cuenta.")

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta del cliente: ")
    balance = float(input("Ingrese el balance inicial del cliente: "))

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

def inicio():
    cliente = crear_cliente()

    while True:
        print("\n¿Qué acción desea realizar?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

        print(cliente)

inicio()
