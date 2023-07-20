# class Usuario:
#     pass

# michael = Usuario()
# anna = Usuario()

# declarar una clase y darle el nombre Usuario
# class Usuario:		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.balance_cuenta = 0

# guido = Usuario()
# monty = Usuario()
# # Accediendo a los atributos de la instancia
# print(guido.name)	# salida: Michael
# print(monty.name)	# salida: Michael

# class Usuario:
#     # Atributo de clase
#     nombre_banco = "Primer Dojo Nacional"

#     # Constructor
#     def __init__(self, name, email_address):
#         # Atributos de instancia
#         self.name = name
#         self.email = email_address
#         self.balance_cuenta = 0

# def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
#         self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
# # método de clase para cambiar el nombre del banco

class CuentaBancaria:
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    def __init__(self, int_rate, balance):
        self.tasa_int = int_rate
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def re_tiro(self, amount):
        # Podemos usar el método estático aquí para evaluar
        # si podemos retirar los fondos sin quedar con balance negativo
        if CuentaBancaria.puede_retirar(self.balance, amount):
            self.balance -= amount
        else:
            print("Fondos insuficientes")
        return self

    # Los métodos estáticos no tienen acceso a ningún atributo
    # solo a lo que se le pasa
    @staticmethod
    def puede_retirar(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def cambiar_nombre_banco(cls, name):
        cls.nombre_banco = name

    @classmethod
    def todos_los_balances(cls):
        sum = 0
        for account in cls.todas_las_cuentas:
            sum += account.balance
        return sum


