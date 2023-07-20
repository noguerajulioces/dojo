class User:
    # Atributo de clase
    bank_name = "Primer Dojo Nacional"

    # Constructor
    def __init__(self, name, email_address):
        # Atributos de instancia
        self.name = name
        self.email = email_address
        self.balance_account = 0

    def make_deposit(self, amount):
        # Método para realizar depósitos
        self.balance_account += amount

    def withdraw_money(self, amount):
        # Método para retirar dinero
        self.balance_account -= amount

    def show_user_balance(self):
        # Método para mostrar el balance del usuario
        print(f"Usuario: {self.name}, Balance: ${self.balance_account}")

    def transfer_money(self, other_user, amount):
        # Método para transferir dinero a otro usuario
        self.balance_account -= amount
        other_user.balance_account += amount


# Ejemplo de uso
user1 = User("Maria Jazmin Barreto", "jazbarreto@python.com")
user2 = User("Cleopatra Python", "cleo@python.com")
user3 = User("Anubis Python, anubis@python.com")

user1.make_deposit(200)  # Depósito de $200 en user1
user1.make_deposit(50)   # Depósito adicional de $50 en user1
user1.make_deposit(350)   # Depósito adicional de $350 en user1
user1.transfer_money(user2, 50)  # Transfiere $50 de user1 a user2
user1.show_user_balance()  # Muestra el balance actualizado de user1

user2.make_deposit(150)   # Depósito de $150 en user2
user2.make_deposit(50)   # Depósito adicional de $50 en user2
user2.transfer_money(user1, 50)  # Transfiere $50 de user2 a user1
user2.transfer_money(user1, 50)  # Transfiere $50 de user2 a user1
user2.show_user_balance()  # Muestra el balance actualizado de user2

user3.make_deposit(650)   # Depósito de $650 en user3
user3.transfer_money(user1, 150)  # Transfiere $150 de user3 a user1
user3.transfer_money(user2, 350)  # Transfiere $350 de user3 a user2
user3.show_user_balance()  # Muestra el balance actualizado de user3