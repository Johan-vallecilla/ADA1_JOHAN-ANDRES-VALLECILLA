import tkinter as tk
from tkinter import ttk, messagebox

# ===========================
# DATOS INICIALES
# ===========================
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

# ===========================
# FUNCIONES DE BÚSQUEDA
# ===========================
def buscar_producto_nombre(nombre):
    return [p for p in productos if nombre.lower() in p['nombre'].lower()]

def buscar_producto_marca(marca):
    return [p for p in productos if marca.lower() in p['marca'].lower()]

def buscar_producto_categoria(categoria):
    return [p for p in productos if categoria.lower() in p['categoria'].lower()]

def buscar_disponibles():
    return [p for p in productos if p['stock'] > 0]

def buscar_empleado_nombre(nombre):
    return [e for e in empleados if nombre.lower() in e['nombre'].lower()]

def buscar_empleado_id(emp_id):
    return [e for e in empleados if str(e['id']) == str(emp_id)]

def buscar_empleado_departamento(depto):
    return [e for e in empleados if depto.lower() in e['departamento'].lower()]


# ===========================
# INTERFAZ GRÁFICA
# ===========================
root = tk.Tk()
root.title("🏬 Sistema de Gestión Valle - Tienda Electrónica")
root.geometry("950x600")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
style.configure("TButton", font=("Arial", 10, "bold"), padding=5)

# ---------------------------
# PESTAÑAS PRINCIPALES
# ---------------------------
tabs = ttk.Notebook(root)
tab_productos = ttk.Frame(tabs)
tab_empleados = ttk.Frame(tabs)
tabs.add(tab_productos, text="🛒 Productos")
tabs.add(tab_empleados, text="👨‍💼 Empleados")
tabs.pack(expand=True, fill="both")


# ===========================
# FUNCIÓN GENERAL DE TABLAS
# ===========================
def limpiar_tabla(tabla):
    for i in tabla.get_children():
        tabla.delete(i)

# ===========================
# PRODUCTOS
# ===========================
frame_p = ttk.LabelFrame(tab_productos, text="Búsqueda de Productos", padding=10)
frame_p.pack(fill="x", padx=10, pady=10)

tk.Label(frame_p, text="Buscar por:").grid(row=0, column=0, padx=5)
opcion_p = ttk.Combobox(frame_p, values=["Nombre", "Marca", "Categoría", "Disponibles"], state="readonly")
opcion_p.grid(row=0, column=1, padx=5)
opcion_p.current(0)

entry_p = ttk.Entry(frame_p, width=30)
entry_p.grid(row=0, column=2, padx=5)

def ejecutar_busqueda_p():
    criterio = opcion_p.get()
    valor = entry_p.get().strip()
    if criterio == "Nombre":
        resultados = buscar_producto_nombre(valor)
    elif criterio == "Marca":
        resultados = buscar_producto_marca(valor)
    elif criterio == "Categoría":
        resultados = buscar_producto_categoria(valor)
    elif criterio == "Disponibles":
        resultados = buscar_disponibles()
    else:
        resultados = []
    mostrar_resultados_p(resultados)

def mostrar_resultados_p(lista):
    limpiar_tabla(tabla_p)
    for p in lista:
        tabla_p.insert("", "end", values=(
            p['id'], p['nombre'], p['marca'], p['categoria'],
            f"${p['precio']:.2f}", p['stock'], "Sí" if p['disponible'] else "No"
        ))

def reiniciar_tabla_p():
    entry_p.delete(0, tk.END)
    mostrar_resultados_p(productos)

ttk.Button(frame_p, text="Buscar", command=ejecutar_busqueda_p).grid(row=0, column=3, padx=5)
ttk.Button(frame_p, text="Reiniciar", command=reiniciar_tabla_p).grid(row=0, column=4, padx=5)

# Tabla productos
tabla_p = ttk.Treeview(tab_productos, columns=("id", "nombre", "marca", "categoria", "precio", "stock", "disponible"), show="headings", height=15)
for col, txt in zip(("id","nombre","marca","categoria","precio","stock","disponible"),
                    ("ID","Nombre","Marca","Categoría","Precio","Stock","Disponible")):
    tabla_p.heading(col, text=txt)
tabla_p.pack(fill="both", expand=True, padx=10, pady=10)

mostrar_resultados_p(productos)  # Mostrar todos al inicio


# ===========================
# EMPLEADOS
# ===========================
frame_e = ttk.LabelFrame(tab_empleados, text="Búsqueda de Empleados", padding=10)
frame_e.pack(fill="x", padx=10, pady=10)

tk.Label(frame_e, text="Buscar por:").grid(row=0, column=0, padx=5)
opcion_e = ttk.Combobox(frame_e, values=["Nombre", "ID", "Departamento"], state="readonly")
opcion_e.grid(row=0, column=1, padx=5)
opcion_e.current(0)

entry_e = ttk.Entry(frame_e, width=30)
entry_e.grid(row=0, column=2, padx=5)

def ejecutar_busqueda_e():
    criterio = opcion_e.get()
    valor = entry_e.get().strip()
    if criterio == "Nombre":
        resultados = buscar_empleado_nombre(valor)
    elif criterio == "ID":
        resultados = buscar_empleado_id(valor)
    elif criterio == "Departamento":
        resultados = buscar_empleado_departamento(valor)
    else:
        resultados = []
    mostrar_resultados_e(resultados)

def mostrar_resultados_e(lista):
    limpiar_tabla(tabla_e)
    for e in lista:
        tabla_e.insert("", "end", values=(
            e['id'], f"{e['nombre']} {e['apellido']}", e['departamento'],
            f"${e['salario']:.2f}", "Activo" if e['activo'] else "Inactivo"
        ))

def reiniciar_tabla_e():
    entry_e.delete(0, tk.END)
    mostrar_resultados_e(empleados)

ttk.Button(frame_e, text="Buscar", command=ejecutar_busqueda_e).grid(row=0, column=3, padx=5)
ttk.Button(frame_e, text="Reiniciar", command=reiniciar_tabla_e).grid(row=0, column=4, padx=5)

# Tabla empleados
tabla_e = ttk.Treeview(tab_empleados, columns=("id", "nombre", "departamento", "salario", "estado"), show="headings", height=15)
for col, txt in zip(("id","nombre","departamento","salario","estado"),
                    ("ID","Nombre Completo","Departamento","Salario","Estado")):
    tabla_e.heading(col, text=txt)
tabla_e.pack(fill="both", expand=True, padx=10, pady=10)

mostrar_resultados_e(empleados)  # Mostrar todos al inicio

# ===========================
# INICIO DE LA APLICACIÓN
# ===========================
root.mainloop()
