import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        sentencia = 'UPDATE persona SET nombre=?, apellido=?, email=? WHERE id_persona=?'
        valores = (
            ("Juan Carlos", "Roldan", "rcarlos@gmail.com", 4), #modifica lo que haya en el id por estos datos que ponemos
            ("Romina", "Ayala", "ayalar@gmail.com", 5) #ídem pero modifica lo que haya en el id 5
        )
        cursor.executemany(sentencia, valores)
        registros_actualizados = cursor.rowcount
        print(f"Se actualizaron los registros: {registros_actualizados}")

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()