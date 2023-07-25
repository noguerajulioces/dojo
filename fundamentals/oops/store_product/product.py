class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = None  # Added for Bonus Sensei

    def update_price(self, percentage_change, is_high):
        if is_high:
            self.price += self.price * (percentage_change / 100)
        else:
            self.price -= self.price * (percentage_change / 100)

    def print_info(self):
        print(f"Nombre: {self.name}")
        print(f"Categoría: {self.category}")
        print(f"Precio: {self.price}")