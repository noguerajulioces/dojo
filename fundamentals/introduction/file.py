num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #Data Types- Primitive- Boolean
string = 'Hello World' #Data Types- Primitive- Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Data Types- Composite -List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Data Types- Composite -Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Data Types- Composite -Tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #Data Types- Composite -list -access value + log statement
pizza_toppings.append('Mushrooms') #Data Types- Composite -List -add value at the end (es una lista porque si era tupla no se iba a poder modificar el valor)
print(person['name']) #Data Types- Composite -Dictionary -access value (arriba esta definido person en dictionary) + log statement 
person['name'] = 'George' #Data Types- Composite -Dictionary -changes value
person['eye_color'] = 'blue' #Data Types- Composite -Dictionary -add value
print(fruit[2]) #Data Types- Composite -Tuples -access value + log statement

if num1 > 45: #conditional if and else + log statement
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #conditional if, elif, else with + length check + log statement
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop from 0 to 4 no considering 5 + log statement x
    print(x)
for x in range(2,5): #for loop from 2 to 4 no considering 5 + log statement x
    print(x)
for x in range(2,10,3): #for loop from 2 to 10 no considering 10 and 3 by 3 + log statement x
    print(x)
x = 0 #variable declaration but is not used in any loop
while(x < 5): #while loop, true when x is lower than 5 + log statement x and increases x by one until x is no more lower than 5
    print(x)
    x += 1

pizza_toppings.pop() #Data Types- Composite -List -delete value (al no tener argumento, eliminirá el último valor de la lista)
pizza_toppings.pop(1) #Data Types- Composite -List -delete value 1

print(person) #Data Types- Composite -Dictionary log statement, delete value eye_color, log statement without eye_color
person.pop('eye_color')
print(person)

for topping in pizza_toppings: #el bucle itera en los elementos de pizza toppings y entra en una condicional que considera a topping
    if topping == 'Pepperoni': #si topping es igual a pepperoni, se continua iterando en el resto de los elementos  sin ejecutar el codigo de abajo
        continue
    print('After 1st if statement') #si el valor de topping no es peperoni se imprimira esa oracion 
    if topping == 'Olives': #en caso de que topping sea olives, se rompe el for y se corta la iteración 
        break

def print_hello_ten_times(): #funcion con un bucle for que imprime hello 10 veces
    for num in range(10):
        print('Hello')

print_hello_ten_times() #agrupa el codigo que imprime los 10 hello

def print_hello_x_times(x): #funcion con un bucle for que imprime hello la cantidad de veces que se indique en el argumento, en este caso, 4
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #hay una funcion con un for x veces, de forma pre determinada, si no tiene argumentos, imprimirá 10 veces hello, si se le da argumentos, imprime la cantidad de veces que tenga el argumento
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

print(num3) #nameError
num3 = 72 #esta desordenado y por lo tanto mal declarado
fruit[0] = 'cranberry' #type error porque fruit es tuple y es inmodificable
print(person['favorite_team']) #key error porque fav team no es una clave que se encuentre 
print(pizza_toppings[7]) #index error porque lo que se pide esta fuera del rango numerico de la lista
print(boolean) #name error porque no esta definido 
fruit.append('raspberry') #atributte error porque fruit es tuple y tuple no tiene el atributo de añadir valor
fruit.pop(1) #atributte error porque fruit es tuple y tuple no tiene el atributo de pop