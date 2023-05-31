import sqlite3 as bd

try:
    conexion = bd.connect("test_db.db") #sqlite no tiene "autocommit = False"
    with conexion:
        cursor = conexion.cursor()
        sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES (?, ?, ?)"
        valores = ("Alex", "rojas", "arojas@gmail.com")
        cursor.execute(sentencia, valores)

        sentencia = "UPDATE persona SET nombre=?, apellido=?, email=? WHERE id_persona = ?"
        valores = ("Juan Carlos", "Roldan", "jcroldan@gmail.com", 15)
        cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
print("Termina la transacción")