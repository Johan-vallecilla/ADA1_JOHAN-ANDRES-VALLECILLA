# Ejemplo sencillo de Quick Sort

def quick_sort(arr):
    """Ordena un arreglo usando el método Quick Sort."""
    if len(arr) <= 1:
        return arr
    pivote = arr[0]
    menores = [x for x in arr[1:] if x < pivote]
    mayores = [x for x in arr[1:] if x >= pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Arreglo de ejemplo
arreglo = [7, 2, 10, 6, 19, 3, 1, 5]

# Ordenar el arreglo
arreglo_ordenado = quick_sort(arreglo)

print("Arreglo ordenado:", arreglo_ordenado)
print("Complejidad: O(n^2) ")