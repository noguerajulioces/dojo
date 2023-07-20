class User:
    # Atributo de clase
    bank_name = "Primer Dojo Nacional"

    # Constructor
    def __init__(self, name, email_address):
        # Atributos de instancia
        self.name = name
        self.email = email_address
        self.cuentas = []  # Lista para almacenar varias cuentas

    def create_account(self, interes, balance=0):
        new_account = CuentaBancaria(interes, balance)
        self.cuentas.append(new_account)
        return new_account

    def make_deposit(self, account_index, amount):
        # Método para realizar depósitos
        self.cuentas[account_index].deposito(amount)
        return self

    def withdraw_money(self, account_index, amount):
        # Método para retirar dinero
        self.cuentas[account_index].retiro(amount)
        return self

    def show_user_balance(self):
        # Método para mostrar el balance del usuario
        print(f"Usuario: {self.name}")
        for idx, cuenta in enumerate(self.cuentas, 1):
            print(f"Cuenta {idx} - Balance: ${cuenta.balance}")

    def transfer_money(self, account_from, other_user, account_to, amount):
        # Método para transferir dinero a otro usuario
        self.cuentas[account_from].retiro(amount)
        other_user.cuentas[account_to].deposito(amount)
        return self


class CuentaBancaria:
    todas_las_cuentas = []

    def __init__(self, interes, balance=0):
        self.interes = interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

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

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            cuenta.mostrar_info_cuenta()

# Creamos dos usuarios
usuario1 = User("Juan", "juan@example.com")
usuario2 = User("María", "maria@example.com")

# Creamos cuentas bancarias para cada usuario con diferentes tasas de interés
cuenta1_usuario1 = usuario1.create_account(interes=0.01, balance=1000)
cuenta2_usuario1 = usuario1.create_account(interes=0.02, balance=500)
cuenta1_usuario2 = usuario2.create_account(interes=0.015, balance=800)

# Mostramos la información de las cuentas de cada usuario
usuario1.show_user_balance()

usuario2.show_user_balance()

# Realizamos operaciones en las cuentas de los usuarios
usuario1.make_deposit(0, 200).withdraw_money(1, 100).transfer_money(1, usuario2, 0, 300)

# Mostramos la información actualizada de las cuentas de cada usuario
usuario1.show_user_balance()

usuario2.show_user_balance()

