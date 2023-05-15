import psycopg2 # Esto es para conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT id_persona, nombre FROM persona'
            cursor.execute(sentencia) # De esta manera ejectutamos la sentencia
            registros = cursor.fetchall() # Recuperamos todos los registros que serán de una lista
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
