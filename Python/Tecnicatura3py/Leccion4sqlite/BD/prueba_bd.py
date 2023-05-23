import sqlite3

conexion = sqlite3.connect("test_db.db")

cursor = conexion.cursor()
sentencia = "SELECT * FROM persona"
cursor.execute(sentencia)
registros = cursor.fetchall()
#print(registros)

for id in registros:
    print(id)

cursor.close()
conexion.close()