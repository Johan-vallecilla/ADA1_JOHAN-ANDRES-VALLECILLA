import sqlite3

def obtener_personas(nombre_db):
    with sqlite3.connect(nombre_db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, direccion, telefono, email, fecha_nacimiento FROM personas")
        columnas = ["id", "nombre", "direccion", "telefono", "email", "fecha_nacimiento"]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

def filtrar_personas(personas, atributo, valor):
    def recursivo(lista):
        if not lista:
            return []
        if len(lista) == 1:
            return [lista[0]] if str(lista[0][atributo]).startswith(valor) else []
        mitad = len(lista) // 2
        return recursivo(lista[:mitad]) + recursivo(lista[mitad:])
    return recursivo(personas)

if __name__ == "__main__":
    personas = obtener_personas("personas.db")
    atributos = ["id", "nombre", "direccion", "telefono", "email", "fecha_nacimiento"]
    print("Atributos disponibles para filtrar:", ", ".join(atributos))
    atributo = input("¿Por qué atributo quieres filtrar?: ").strip()
    valor = input("¿Qué valor debe tener (o empezar con)?: ").strip()
    if atributo not in atributos:
        print("Atributo no válido.")
    else:
        resultados = filtrar_personas(personas, atributo, valor)
        print("Resultados encontrados:", len(resultados))
        for r in resultados[:10]:
            print(r)