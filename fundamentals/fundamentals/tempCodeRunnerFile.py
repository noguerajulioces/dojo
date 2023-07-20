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