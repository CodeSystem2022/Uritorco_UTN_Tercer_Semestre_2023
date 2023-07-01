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
        cursor = conexion.cursor()
        ver_id()
        sentencia = 'UPDATE deudor SET deuda=? WHERE id=?'
        id_deudor = int(input("ingrese el ID del deudor que desea editar: "))
        monto_deudor = float(input("Ingrese el monto nuevo: "))
        valores = (monto_deudor, id_deudor)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print(f"Se actualizó el monto")
        import ver_deudores

except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
