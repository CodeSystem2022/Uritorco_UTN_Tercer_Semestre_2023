import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        sentencia = 'UPDATE persona SET nombre=?, apellido=?, email=? WHERE id_persona=?'
        valores = ("Juan Carlos", "Roldan", "rcarlos@gmail.com", "1")
        cursor.execute(sentencia, valores)
        registros_actualizados = cursor.rowcount
        print(f"Se actualizaron los registros: {registros_actualizados}")

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()