import sqlite3

blue_text = "\033[94m"
reset_text = "\033[0m"

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
            print("- - - Deudas - - -")
            for registro in registros:
                print("|  ",
                      registro[1], blue_text,
                      " - $",
                      registro[2], reset_text)

except Exception as e:
    print(f'Ha ocurrido un error: {e}')