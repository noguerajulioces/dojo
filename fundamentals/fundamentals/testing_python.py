import random #se importa el módulo random, que proporciona funciones relacionadas con la generación de números aleatorios.

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #Se define una lista llamada "weekdays" que contiene los días de la semana. Luego, se utiliza la función random.choice para seleccionar de forma aleatoria un elemento de la lista "weekdays" y se asigna a la variable "day".
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')
