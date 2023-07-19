#basica
y = 0

while y <= 150:
    print(y)
    y += 1

#Múltiplos de cinco:
number = 5

while number<= 1000:
    print(number)
    number += 5

#Contar, a la manera del Dojo: 
for numero in range(1, 101):
    if numero % 10 == 0:
        print("Coding Dojo")
    elif numero % 5 == 0:
        print("Coding")
    else:
        print(numero)

#Whoa. Es un gran idiota
suma = 0

for numero in range(1, 500001, 2):
    suma += numero
print("La suma de los enteros impares es:", suma)

#Cuenta regresiva de a 4
numero = 2018

while numero > 0:
    print(numero)
    numero -= 4

#Contador flexible
lowNum = 2
highNum = 9
mult = 3

for numero in range(lowNum, highNum + 1):
    if numero % mult == 0:
        print(numero)