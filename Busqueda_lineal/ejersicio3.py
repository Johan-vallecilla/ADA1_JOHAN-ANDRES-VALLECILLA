empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]


# 🔍 1. Buscar por nombre completo
def buscar_por_nombre_completo(nombre, apellido):
    resultados = []
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre.lower() and empleado['apellido'].lower() == apellido.lower():
            resultados.append(empleado)
    return resultados


# 🔍 2. Buscar por departamento
def buscar_por_departamento(departamento):
    resultados = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento.lower():
            resultados.append(empleado)
    return resultados


# 🔍 3. Buscar empleados activos
def buscar_empleados_activos(activo=True):
    """
    Parámetro:
      activo = True  → busca empleados activos
      activo = False → busca empleados inactivos
    """
    resultados = []
    for empleado in empleados:
        if empleado['activo'] == activo:
            resultados.append(empleado)
    return resultados


# 🧪 Ejemplos de uso:
print("🔹 Buscar por nombre completo:")
print(buscar_por_nombre_completo("Ana", "García"))

print("\n🔹 Buscar por departamento:")
print(buscar_por_departamento("Ventas"))

print("\n🔹 Buscar empleados activos:")
print(buscar_empleados_activos(False))
