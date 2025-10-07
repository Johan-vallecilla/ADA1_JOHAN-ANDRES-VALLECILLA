import sqlite3

# Lee el archivo SQL
with open("personas_desordenadas.sql", encoding="utf-8") as f:
    sql_script = f.read()

# Crea la base de datos y ejecuta el script
conn = sqlite3.connect("personas.db")
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Base de datos personas.db creada y poblada con éxito.")