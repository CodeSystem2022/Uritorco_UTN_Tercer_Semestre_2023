import sqlite3 as bd

conexion = bd.connect("deudor.db")

try:
    cursor = conexion.cursor()
    sentencia = "INSERT INTO deudor (nombre, deuda) VALUES (?, ?)"
    nombre_deudor = input("Ingrese el nombre de la persona: ")
    monto_deudor = float(input("Ingrese el monto de la deuda: "))
    valores = (nombre_deudor, monto_deudor)
    cursor.execute(sentencia, valores)
    conexion.commit()  # Commit the transaction
    print(f"Se ha agregado un monto de {monto_deudor}")

except Exception as e:
    conexion.rollback()
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()