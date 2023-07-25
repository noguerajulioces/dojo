# implementa __init__( name , tipo , golosinas ):
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
# comer() - incrementa la energía de la mascota en 5 y la salud en 10
# jugar() - incrementa la salud de la mascota en 5
# ruido() - imprime el sonido que produce la mascota
class Mascota:
    def __init__(self, name, type, candy):
        self.name = name
        self.type = type
        self.candy = candy
        self.energy = 100
        self.health = 100

    def sleep(self):
        self.energy += 25
        print(f"{self.name} está durmiendo. Energía aumentada en 25.")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} está comiendo. Energía aumentada en 5 y salud aumentada en 10.")

    def play(self):
        self.health += 5
        print(f"{self.name} está jugando. Salud aumentada en 5.")

    def sound(self):
        print(f"{self.name} hace un sonido: ¡{self.type}!")


#herencia para crear subclases de mascotas
class Dog(Mascota):
    def __init__(self, name, candy):
        super().__init__(name, "guau", candy)  #en esta parte se llama al constructor de la clase 

    def play_fetch(self):
        print(f"{self.name} está jugando a buscar la pelota.")

class Cat(Mascota):
    def __init__(self, name, candy):
        super().__init__(name, "miau", candy)  #en esta parte se llama al constructor de la clase 

    def sleep_in_box(self):
        print(f"{self.name} está durmiendo cómodamente en una caja.")