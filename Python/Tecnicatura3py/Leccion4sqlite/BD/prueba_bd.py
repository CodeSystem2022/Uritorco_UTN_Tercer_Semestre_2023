import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        sentencia = 'SELECT * FROM persona WHERE id_persona = ?'      #%s -> ${var}
        id_persona = input("Ingrese el id de la persona que desea consultar")
        cursor.execute(sentencia, (id_persona,))
        registros = cursor.fetchall()
        print(registros)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()