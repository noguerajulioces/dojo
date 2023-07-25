class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, product_id):
        if 0 <= product_id < len(self.products):
            product = self.products.pop(product_id)
            product.print_info()
        else:
            print("¡Producto no encontrado!")

    def inflation(self, percentage_increase):
        for product in self.products:
            product.update_price(percentage_increase, True)

    def clearance_sale(self, category, percentage_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percentage_discount, False)

    def print_products(self):
        print(f"Productos en {self.name}:")
        for i, product in enumerate(self.products):
            print(f"ID: {i}")
            product.print_info()
            print("-" * 30)