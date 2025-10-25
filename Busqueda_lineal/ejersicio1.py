def busqueda_lineal_simple(lista, objetivo):

    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1



numeros = [64, 34, 25, 12, 22, 11, 90]
print(busqueda_lineal_simple(numeros, 25))  # Debe retornar 2
print(busqueda_lineal_simple(numeros, 99))  # Debe retornar -1
