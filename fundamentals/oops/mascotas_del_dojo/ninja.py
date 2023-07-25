# implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()

class Ninja:
    def __init__(self, name, lastName, prize, food_pet, pet):
        self.name = name
        self.lastName = lastName
        self.prize = prize
        self.food_pet = food_pet
        self.pet = pet

    def walk(self):
        print(f"Estamos paseando a {self.pet.name}!")

    def feeding(self):
        print(f"Estamos alimentando a {self.pet.name}!")

    def bathe(self):
        print(f"Estamos bañando a {self.pet.name}!")