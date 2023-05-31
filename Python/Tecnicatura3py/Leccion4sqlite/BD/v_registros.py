import sqlite3

try:
    conexion = sqlite3.connect("test_db.db")
    with conexion:
        cursor = conexion.cursor()
        entrada = input("Ingrese los id de persona para buscar, separado por coma: ")
        claves_primarias = (tuple(entrada.split(',')),)
        sentencia = 'SELECT * FROM persona WHERE id_persona IN ({})'.format(','.join(['?' for _ in claves_primarias[0]])) #query vieja
        cursor.execute(sentencia, claves_primarias[0])
        #conexion.commit() <- esto se hace automáticamente en el with. Sería para guardar los cambios
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()



# %s -> ${var}