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
        return self

    def withdraw_money(self, amount):
        # Método para retirar dinero
        self.balance_account -= amount
        return self

    def show_user_balance(self):
        # Método para mostrar el balance del usuario
        print(f"Usuario: {self.name}, Balance: ${self.balance_account}")

    def transfer_money(self, other_user, amount):
        # Método para transferir dinero a otro usuario
        self.balance_account -= amount
        other_user.balance_account += amount
        return self


# Ejemplo de uso
user1 = User("Maria Jazmin Barreto", "jazbarreto@python.com")
user2 = User("Cleopatra Python", "cleo@python.com")
user3 = User("Anubis Python", "anubis@python.com")

user1.make_deposit(200).make_deposit(50).make_deposit(350).transfer_money(user2, 50).show_user_balance()

user2.make_deposit(150).make_deposit(50).transfer_money(user1, 50).transfer_money(user1, 50).show_user_balance()

user3.make_deposit(650).transfer_money(user1, 150).transfer_money(user2, 350).show_user_balance()