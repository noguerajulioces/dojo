class CuentaBancaria:
    def __init__(self, interes, balance=0):
        self.interes = interes
        self.balance = balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.interes
        return self

# Crear dos cuentas bancarias
cuenta1 = CuentaBancaria(interes=0.01, balance=1000)
cuenta2 = CuentaBancaria(interes=0.02, balance=500)

# Encadenar las operaciones en una línea
cuenta1.deposito(200).deposito(300).deposito(100).retiro(500).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(100).deposito(200).retiro(50).retiro(100).retiro(150).retiro(50).generar_interes().mostrar_info_cuenta()
