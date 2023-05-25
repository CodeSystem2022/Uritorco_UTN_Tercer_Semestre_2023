import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        entrada = input("Ingrese los números de id del usuario que desea eliminar, separado por coma: ")
        valores = (tuple(entrada.split(','),))
        sentencia = 'DELETE FROM persona WHERE id_persona IN ({})'.format(','.join(['?' for _ in valores]))
        cursor.execute(sentencia, valores)
        registros_eliminados = cursor.rowcount
        print(f"Se eliminaron los registros: {registros_eliminados}")

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()