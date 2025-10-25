# 🛒 Lista de productos
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]


# 🔍 1. Buscar productos disponibles (stock > 0)
def buscar_productos_disponibles():
    disponibles = []
    for producto in productos:
        if producto['stock'] > 0:
            disponibles.append(producto)
    return disponibles


# 🔍 2. Buscar productos por rango de precios
def buscar_por_rango_precio(min_precio, max_precio):
    resultados = []
    for producto in productos:
        if min_precio <= producto['precio'] <= max_precio:
            resultados.append(producto)
    return resultados


# 🔍 3. Buscar productos de una marca específica
def buscar_por_marca(marca):
    resultados = []
    for producto in productos:
        if producto['marca'].lower() == marca.lower():
            resultados.append(producto)
    return resultados


# 🔢 4. Contar productos en una categoría
def contar_por_categoria(categoria):
    contador = 0
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            contador += 1
    return contador


# 🧪 Ejemplos de uso:
print("🔹 Productos disponibles (stock > 0):")
print(buscar_productos_disponibles())

print("\n🔹 Productos entre $500 y $1200:")
print(buscar_por_rango_precio(500, 1200))

print("\n🔹 Productos de la marca Apple:")
print(buscar_por_marca("Apple"))

print("\n🔹 Cantidad de productos en la categoría 'Laptop':")
print(contar_por_categoria("Laptop"))
