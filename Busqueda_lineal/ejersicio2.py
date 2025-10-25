productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]

# 🔍 1. Búsqueda lineal por nombre
def buscar_por_nombre(nombre):
    resultados = []
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            resultados.append(producto)
    return resultados


# 🔍 2. Búsqueda lineal por ID
def buscar_por_id(id_busqueda):
    for producto in productos:
        if producto['id'] == id_busqueda:
            return producto
    return None


# 🔍 3. Búsqueda lineal por categoría
def buscar_por_categoria(categoria):
    resultados = []
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            resultados.append(producto)
    return resultados


# 🧪 Ejemplos de uso:
print("🔹 Buscar por nombre:")
print(buscar_por_nombre("iPhone 15"))

print("\n🔹 Buscar por ID:")
print(buscar_por_id(1))

print("\n🔹 Buscar por categoría:")
print(buscar_por_categoria("Smartphone"))