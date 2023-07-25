from product import Product
from store import Store

#Se crea una instancia de la tienda
my_store = Store("Mi Tienda Natural")

# Creamos instancias de los productos de la tienda
product1 = Product("Remedio para mate", 5000, "Herbs")
product2 = Product("Té de hierbas", 3500, "Herbs")
product3 = Product("Café molido", 2500, "Beverages")

# Agregamos productos a la tienda
my_store.add_product(product1)
my_store.add_product(product2)
my_store.add_product(product3)

# Mostramos los productos en la tienda
my_store.print_products()

# Vendemos un producto por su ID
print("Vendiendo un producto...")
my_store.sell_product(1)

# Aplicamos inflación del 10%
print("Aplicando inflación del 10%...")
my_store.inflation(10)

# Mostramos los productos después de la inflación
my_store.print_products()

# Hacemos una liquidación del 20% en productos de categoría "Herbs"
print("Haciendo liquidación del 20% en productos de categoría 'Herbs'...")
my_store.clearance_sale("Herbs", 20)

# Mostramos los productos después de la liquidación
my_store.print_products()
