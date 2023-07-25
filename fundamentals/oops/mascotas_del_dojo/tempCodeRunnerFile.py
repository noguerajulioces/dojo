from ninja import Ninja
from mascota import Mascota

# Ejemplo de uso
mascota1 = Mascota("Cleo", "miau", "atún")
ninja1 = Ninja("Jazmin", "Barreto", "empanada", "flan", mascota1)

ninja1.walk()
ninja1.feeding()
ninja1.bathe()

mascota1.sleep()
mascota1.eat()
mascota1.play()
mascota1.sound()