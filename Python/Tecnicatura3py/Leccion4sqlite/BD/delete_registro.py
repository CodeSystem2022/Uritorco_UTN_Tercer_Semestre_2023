import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        entrada = input("Ingrese el número de id del usuario que desea eliminar: ")
        sentencia = 'DELETE FROM persona WHERE id_persona = ?'
        valores = (entrada,)
        cursor.execute(sentencia, valores)
        registros_eliminados = cursor.rowcount
        print(f"Se eliminaron los registros: {registros_eliminados}")

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()