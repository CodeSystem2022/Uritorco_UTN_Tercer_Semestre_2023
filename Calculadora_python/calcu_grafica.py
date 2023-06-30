import tkinter as tk
import sqlite3

def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"El resultado de la suma es: {resultado}")

def restar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text=f"El resultado de la resta es: {resultado}")

def multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text=f"El resultado de la multiplicación es: {resultado}")

def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 == 0:
        label_resultado.config(text="Error: División por cero")
    else:
        resultado = num1 / num2
        label_resultado.config(text=f"El resultado de la división es: {resultado}")

def agregar_deudor():
    nombre = entry_nombre.get()
    deuda = float(entry_deuda.get())

    conexion = sqlite3.connect("deudor.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO deudor (nombre, deuda) VALUES (?, ?)", (nombre, deuda))
    conexion.commit()
    conexion.close()

    label_resultado.config(text="Deudor agregado correctamente")

    # Clear entry fields after adding debtor
    entry_nombre.delete(0, tk.END)
    entry_deuda.delete(0, tk.END)

def ver_deudores():
    conexion = sqlite3.connect("deudor.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM deudor")
    deudores = cursor.fetchall()
    conexion.close()

    # Clear the existing debtor list in the text widget
    text_deudores.delete(1.0, tk.END)

    if deudores:
        for deudor in deudores:
            id = deudor[0]
            nombre = deudor[1]
            deuda = deudor[2]
            text_deudores.insert(tk.END, f"ID: {id}, Nombre: {nombre}, Deuda: {deuda}\n")
    else:
        text_deudores.insert(tk.END, "No hay deudores registrados")

window = tk.Tk()
window.title("Calculadora")

label_menu = tk.Label(window, text="|  C a l c u l a d o r a  |")
label_menu.grid(row=0, column=0, columnspan=4)

btn_sumar = tk.Button(window, text="Sumar", command=sumar)
btn_sumar.grid(row=3, column=0, sticky="ew")

btn_restar = tk.Button(window, text="Restar", command=restar)
btn_restar.grid(row=3, column=1, sticky="ew")

btn_multiplicar = tk.Button(window, text="Multiplicar", command=multiplicar)
btn_multiplicar.grid(row=4, column=0, sticky="ew")

btn_dividir = tk.Button(window, text="Dividir", command=dividir)
btn_dividir.grid(row=4, column=1, sticky="ew")

label_num1 = tk.Label(window, text="Primer número:")
label_num1.grid(row=1, column=0)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=1, column=1)

label_num2 = tk.Label(window, text="Segundo número:")
label_num2.grid(row=2, column=0)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=2, column=1)

label_resultado = tk.Label(window)
label_resultado.grid(row=5, column=0, columnspan=4)

label_deudor = tk.Label(window, text="Nombre del deudor:")
label_deudor.grid(row=6, column=0)
entry_nombre = tk.Entry(window)
entry_nombre.grid(row=6, column=1)

label_deuda = tk.Label(window, text="Deuda:")
label_deuda.grid(row=7, column=0)
entry_deuda = tk.Entry(window)
entry_deuda.grid(row=7, column=1)

btn_agregar_deudor = tk.Button(window, text="Agregar deudor", command=agregar_deudor)
btn_agregar_deudor.grid(row=6, column=2, columnspan=2, rowspan=2)

btn_ver_deudores = tk.Button(window, text="Ver deudores", command=ver_deudores)
btn_ver_deudores.grid(row=9, column=0, columnspan=4)

label_deudores = tk.Label(window, text="Lista de deudores:")
label_deudores.grid(row=10, column=0, columnspan=4)
text_deudores = tk.Text(window, height=10, width=40)
text_deudores.grid(row=11, column=0, columnspan=4)

window.mainloop()
