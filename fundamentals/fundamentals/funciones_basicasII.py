#cuenta regresiva
def countdown(number):
    list = []
    while number >= 0:
        list.append(number)
        number -= 1
    return list
#ejemplo del uso
resultado = countdown(5)
print(resultado)
# Salida: [5, 4, 3, 2, 1, 0]

#Imprimir y devolver
def print_and_return(lista):
    print(lista[0])
    return lista[1]
# Ejemplo de uso:
resultado = print_and_return([1, 2])
print(resultado)  
# Salida: 1 (impreso) y 2 (devuelto)

#primero mas longitud
def primero_mas_longitud(lista):
    primer_valor = lista[0]
    longitud_lista = len(lista)
    return primer_valor + longitud_lista

# Ejemplo de uso:
resultado = primero_mas_longitud([1, 2, 3, 4, 5])
print(resultado)  
# Salida: 6 (1 + 5)

#valores mayores que el segundo
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False

    segundo_valor = lista[1]
    nueva_lista = [valor for valor in lista if valor > segundo_valor]
    cantidad_valores = len(nueva_lista)

    print(cantidad_valores)
    return nueva_lista

# Ejemplos de uso:
resultado1 = valores_mayores_que_el_segundo([5, 2, 3, 2, 1, 4])
print(resultado1)  
# Salida: 3, [5, 3, 4]
resultado2 = valores_mayores_que_el_segundo([3])
print(resultado2)  
# Salida: False

#Esta longitud, ese valor
def length_and_value(tamaño, valor):
    nueva_lista = [valor] * tamaño
    return nueva_lista

# Ejemplos de uso:
resultado1 = length_and_value(4, 7)
print(resultado1)  # Salida: [7, 7, 7, 7]

resultado2 = length_and_value(6, 2)
print(resultado2)  # Salida: [2, 2, 2, 2, 2, 2]
