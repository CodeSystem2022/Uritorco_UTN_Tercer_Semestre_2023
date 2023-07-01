import sqlite3

blue_text = "\033[94m"
yellow_text = "\033[93m"
red_text = "\033[91m"
reset_text = "\033[0m"

def ver_id():
    try:
        conexion = sqlite3.connect("deudor.db")
        with conexion:
            cursor = conexion.cursor()
            sentencia = 'SELECT * FROM deudor'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            if len(registros) == 0:
                print(blue_text, "No hay deudas registradas todavía", reset_text)
            else:
                print("- - - Deudores - - -")
                for registro in registros:
                    print("| ID:", red_text, registro[0], reset_text,
                          registro[1], blue_text,
                          " - $",
                          registro[2], reset_text)
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
    finally:
        conexion.close()


try:
    conexion = sqlite3.connect("deudor.db")
    with conexion:
        ver_id()
        cursor = conexion.cursor()
        entrada = input("Ingrese el número de id del usuario que desea eliminar: ")
        sentencia = 'DELETE FROM deudor WHERE id = ?'
        valores = (entrada,)
        print(red_text, f"Está seguro de que desea eliminar al usuario con ID {entrada}?", reset_text,
              f"\n 1. Sí"
              f"\n 2. No")
        if input("Seleccione una opción: ") == "1":
            cursor.execute(sentencia, valores)
            print(f"Se eliminó un deudor")
        else:
            print("Acá no pasó nada, señores")

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()