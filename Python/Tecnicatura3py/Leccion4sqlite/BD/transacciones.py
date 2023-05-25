import sqlite3 as bd

conexion = bd.connect("test_db.db") #sqlite no tiene "autocommit = False"

try:
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES (?, ?, ?)"
    valores = ("María", "Esparza", "mesparza@gmail.com")
    cursor.execute(sentencia, valores)
    #conexion.commit() #se usaría en postgres
    print("Termina la transacción")

except Exception as e:
    conexion.rollback()
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()