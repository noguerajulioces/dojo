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

class Usuario:
    # Atributo de clase
    nombre_banco = "Primer Dojo Nacional"

    # Constructor
    def __init__(self, name, email_address):
        # Atributos de instancia
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0

def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido




