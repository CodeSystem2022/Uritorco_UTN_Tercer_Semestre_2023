import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        #sentencia = 'SELECT * FROM persona WHERE id_persona IN ({})'.format(','.join(['?' for _ in claves_primarias[0]])) #query vieja
        sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (?, ?, ?)'
        valores = (
            ("Carlos", "Lara", "clara@gmail.com"),
            ("Marcos", "Canto", "mcanto@gmail.com"),
            ("Marcelo", "Cuenca", "cuencam@gmail.com")
        )
        cursor.executemany(sentencia, valores)
        #conexion.commit() <- esto se hace automáticamente en el with. Sería para guardar los cambios
        registros_insertados = cursor.rowcount
        print(f"Se insertaron los registros: {registros_insertados}")

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()