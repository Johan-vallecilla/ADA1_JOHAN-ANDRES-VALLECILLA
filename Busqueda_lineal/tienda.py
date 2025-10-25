# ==============================
# 🏬 SISTEMA DE GESTIÓN TIENDA "VALLE" (Versión mejorada)
# ==============================

# --- Estructuras base ---
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]

# ==============================
# 🔍 FUNCIONES DE PRODUCTOS
# ==============================

def buscar_producto_por_nombre(nombre):
    nombre = nombre.lower()
    return [p for p in productos if nombre in p['nombre'].lower()]

def buscar_producto_por_marca(marca):
    marca = marca.lower()
    return [p for p in productos if marca in p['marca'].lower()]

def buscar_producto_por_categoria(categoria):
    categoria = categoria.lower()
    return [p for p in productos if categoria in p['categoria'].lower()]

def buscar_productos_disponibles():
    return [p for p in productos if p['stock'] > 0]

def actualizar_stock(id_producto, nuevo_stock):
    for p in productos:
        if p['id'] == id_producto:
            p['stock'] = nuevo_stock
            p['disponible'] = nuevo_stock > 0
            print(f"\n✅ Stock del producto '{p['nombre']}' actualizado a {nuevo_stock}.")
            return
    print("❌ Producto no encontrado.")

# ==============================
# 👨‍💼 FUNCIONES DE EMPLEADOS
# ==============================

def buscar_empleado_por_nombre(nombre):
    nombre = nombre.lower()
    return [e for e in empleados if nombre in e['nombre'].lower()]

def buscar_empleado_por_id(id_busqueda):
    for e in empleados:
        if e['id'] == id_busqueda:
            return e
    return None

def buscar_empleado_por_departamento(depto):
    depto = depto.lower()
    return [e for e in empleados if depto in e['departamento'].lower()]

# ==============================
# 🧾 FUNCIONES AUXILIARES
# ==============================

def mostrar_productos(lista):
    if not lista:
        print("\n⚠️ No se encontraron productos.")
    else:
        print("\n📦 Productos encontrados:")
        for p in lista:
            print(f"  ID: {p['id']} | {p['nombre']} | Marca: {p['marca']} | "
                  f"Categoría: {p['categoria']} | Precio: ${p['precio']} | Stock: {p['stock']} | Disponible: {p['disponible']}")

def mostrar_empleados(lista):
    if not lista:
        print("\n⚠️ No se encontraron empleados.")
    else:
        print("\n👤 Empleados encontrados:")
        for e in lista:
            estado = "Activo" if e['activo'] else "Inactivo"
            print(f"  ID: {e['id']} | {e['nombre']} {e['apellido']} | Depto: {e['departamento']} | "
                  f"Salario: ${e['salario']} | Estado: {estado}")

# ==============================
# 🧭 MENÚS INTERACTIVOS
# ==============================

def menu_productos():
    while True:
        print("\n====== 🛒 MENÚ DE PRODUCTOS ======")
        print("1. Buscar por nombre")
        print("2. Buscar por marca")
        print("3. Buscar por categoría")
        print("4. Ver productos disponibles (stock > 0)")
        print("5. Actualizar stock de un producto")
        print("6. Volver al menú principal")
        print("=================================")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre o parte del nombre del producto: ")
            mostrar_productos(buscar_producto_por_nombre(nombre))
        elif opcion == "2":
            marca = input("Ingrese la marca: ")
            mostrar_productos(buscar_producto_por_marca(marca))
        elif opcion == "3":
            categoria = input("Ingrese la categoría: ")
            mostrar_productos(buscar_producto_por_categoria(categoria))
        elif opcion == "4":
            mostrar_productos(buscar_productos_disponibles())
        elif opcion == "5":
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                actualizar_stock(id_prod, nuevo_stock)
            except ValueError:
                print("❌ Error: ingrese valores numéricos válidos.")
        elif opcion == "6":
            break
        else:
            print("❌ Opción no válida.")

def menu_empleados():
    while True:
        print("\n====== 👨‍💼 MENÚ DE EMPLEADOS ======")
        print("1. Buscar por nombre")
        print("2. Buscar por ID")
        print("3. Buscar por departamento")
        print("4. Volver al menú principal")
        print("==================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre o parte del nombre: ")
            mostrar_empleados(buscar_empleado_por_nombre(nombre))
        elif opcion == "2":
            try:
                id_emp = int(input("Ingrese el ID del empleado: "))
                empleado = buscar_empleado_por_id(id_emp)
                mostrar_empleados([empleado] if empleado else [])
            except ValueError:
                print("❌ Error: el ID debe ser numérico.")
        elif opcion == "3":
            depto = input("Ingrese el nombre o parte del nombre del departamento: ")
            mostrar_empleados(buscar_empleado_por_departamento(depto))
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")

# ==============================
# 🏠 MENÚ PRINCIPAL
# ==============================

def menu_principal():
    while True:
        print("\n==============================")
        print("🏬 SISTEMA DE TIENDA 'VALLE'")
        print("==============================")
        print("1. Gestión de productos")
        print("2. Gestión de empleados")
        print("3. Salir del sistema")
        print("==============================")

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            print("\n👋 Gracias por usar el sistema de la Tienda Valle. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")

# ==============================
# 🚀 EJECUCIÓN DEL SISTEMA
# ==============================
menu_principal()
