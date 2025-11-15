import csv

# Nombres de archivos
ARCHIVO_ENTRADA = 'productos.csv'
ARCHIVO_SALIDA = 'productos_ordenados.csv'

def merge_sort(lista, idx_calif, idx_precio):
    """Ordena la lista usando Merge Sort por calificación (desc) y precio (asc)."""
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad], idx_calif, idx_precio)
    derecha = merge_sort(lista[mitad:], idx_calif, idx_precio)
    return merge(izquierda, derecha, idx_calif, idx_precio)

def merge(izq, der, idx_calif, idx_precio):
    """Fusiona dos listas ordenadas según los criterios."""
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        try:
            calif_i = float(izq[i][idx_calif])
            calif_j = float(der[j][idx_calif])
            precio_i = float(izq[i][idx_precio])
            precio_j = float(der[j][idx_precio])
        except:
            resultado.append(izq[i])
            i += 1
            continue
        # Ordenar por calificación descendente, luego precio ascendente
        if calif_i > calif_j or (calif_i == calif_j and precio_i <= precio_j):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado += izq[i:]
    resultado += der[j:]
    return resultado

def ordenar_csv(entrada, salida):
    """Lee un CSV, lo ordena, guarda el resultado y muestra los 10 mejores productos."""
    with open(entrada, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        encabezado = next(lector)
        filas = list(lector)
    # Buscar índices de columnas
    idx_calif = encabezado.index('calificacion')
    idx_precio = encabezado.index('precio')
    # Ordenar
    filas_ordenadas = merge_sort(filas, idx_calif, idx_precio)
    # Guardar resultado
    with open(salida, 'w', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(encabezado)
        escritor.writerows(filas_ordenadas)
    print(f"Archivo '{salida}' creado correctamente.\n")
    # Imprimir los 10 mejores productos
    print("Top 10 productos:")
    print(" | ".join(encabezado))
    for fila in filas_ordenadas[:10]:
        print(" | ".join(fila))

# Ejecutar
ordenar_csv(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)