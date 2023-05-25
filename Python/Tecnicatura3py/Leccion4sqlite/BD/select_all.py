import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        sentencia = 'SELECT * FROM persona'
        cursor.execute(sentencia)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()