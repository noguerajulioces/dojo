# Ejemplo de uso
# mascota1 = Mascota("Cleo", "miau", "atún")
# ninja1 = Ninja("Jazmin", "Barreto", "empanada", "flan", mascota1)

# ninja1.walk()
# ninja1.feeding()
# ninja1.bathe()

# mascota1.sleep()
# mascota1.eat()
# mascota1.play()
# mascota1.sound()
from ninja import Ninja
from mascota import Mascota
from mascota import Dog, Cat  # Importar las clases Dog y Cat desde el módulo mascota

perro1 = Dog("Whisky", "hueso")
gato1 = Cat("Anubis", "pescado")

perro1.sound()          # Salida: "Whisky hace un sonido: ¡guau!"
gato1.sound()           # Salida: "Anubis hace un sonido: ¡miau!"

perro1.play_fetch()     # Salida: "Whisky está jugando a buscar la pelota."
gato1.sleep_in_box()    # Salida: "Anubis está durmiendo cómodamente en una caja."

perro1.sleep()          # Salida: "Whisky está durmiendo. Energía aumentada en 25."
gato1.eat()             # Salida: "Anubis está comiendo. Energía aumentada en 5 y salud aumentada en 10."