# 🛒 Lista de productos
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]

# === FUNCIONES DE BÚSQUEDA ===

def buscar_productos_disponibles():
    return [p for p in productos if p['stock'] > 0]


def buscar_por_rango_precio(min_precio, max_precio):
    return [p for p in productos if min_precio <= p['precio'] <= max_precio]


def buscar_por_marca(marca):
    return [p for p in productos if p['marca'].lower() == marca.lower()]


def contar_por_categoria(categoria):
    return sum(1 for p in productos if p['categoria'].lower() == categoria.lower())


# === FUNCIONES DE UTILIDAD ===

def mostrar_productos(lista):
    """Muestra productos de forma ordenada"""
    if not lista:
        print("\n⚠️ No se encontraron productos.")
    else:
        print("\n📦 Productos encontrados:")
        for p in lista:
            print(f"  ID: {p['id']} | {p['nombre']} | Marca: {p['marca']} | "
                  f"Categoría: {p['categoria']} | Precio: ${p['precio']} | Stock: {p['stock']}")


# === MENÚ PRINCIPAL ===

def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Buscar productos disponibles")
        print("2. Buscar productos por rango de precios")
        print("3. Buscar productos por marca")
        print("4. Contar productos en una categoría")
        print("5. Salir")
        print("====================================")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            disponibles = buscar_productos_disponibles()
            mostrar_productos(disponibles)

        elif opcion == "2":
            try:
                min_precio = float(input("Ingrese el precio mínimo: "))
                max_precio = float(input("Ingrese el precio máximo: "))
                resultados = buscar_por_rango_precio(min_precio, max_precio)
                mostrar_productos(resultados)
            except ValueError:
                print("❌ Error: debe ingresar valores numéricos.")

        elif opcion == "3":
            marca = input("Ingrese la marca que desea buscar: ")
            resultados = buscar_por_marca(marca)
            mostrar_productos(resultados)

        elif opcion == "4":
            categoria = input("Ingrese la categoría: ")
            cantidad = contar_por_categoria(categoria)
            print(f"\n📊 Hay {cantidad} producto(s) en la categoría '{categoria}'.")
            
        elif opcion == "5":
            print("\n👋 Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")


# === EJECUCIÓN DEL PROGRAMA ===
menu_principal()
