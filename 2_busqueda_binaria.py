# Ejemplo sencillo de búsqueda binaria

def busqueda_binaria(arr, objetivo):
    """Busca un elemento en un arreglo ordenado usando búsqueda binaria."""
    izquierda = 0
    derecha = len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio  # Retorna la posición donde se encontró
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No se encontró el elemento

# Arreglo de ejemplo
arreglo = [2, 4, 7, 10, 15]
numero_a_buscar = 7

# Buscar el número
resultado = busqueda_binaria(arreglo, numero_a_buscar)

if resultado != -1:
    print(f"El número {numero_a_buscar} está en la posición {resultado}.")
else:
    print("El número no está en el arreglo.")

print("Complejidad Final: O(log n)")