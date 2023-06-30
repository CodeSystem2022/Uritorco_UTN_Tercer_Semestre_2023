# ANSI
yellow_text = "\033[93m"
reset_text = "\033[0m"

# Función de suma
def sumar(num1, num2):
    return num1 + num2

# Función de resta
def restar(num1, num2):
    return num1 - num2

# Función de multiplicación
def multiplicar(num1, num2):
    return num1 * num2

# Función de división
def dividir(num1, num2):
    if num2 == 0:
        return "Error: División por cero"
    else:
        return num1 / num2

# Función para mostrar el menú de opciones
def mostrar_menu():
    print(yellow_text, "| MENÚ |", reset_text)
    print(yellow_text,"|1|", reset_text, "Sumar")
    print(yellow_text,"|2|", reset_text, "Restar")
    print(yellow_text,"|3|", reset_text, "Multiplicar")
    print(yellow_text,"|4|", reset_text, "Dividir")
    print(yellow_text,"|5|", reset_text, "Deudores")
    print(yellow_text,"|6|", reset_text, "Salir")

# Ciclo principal

def consultar_deudores():
    print("1. Ver deudores")
    print("2. Agregar deudor")
    print("3. Editar deudor")
    print("4. Eliminar deudor")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        import ver_deudores
    elif opcion == "2":
        import agregar_deudor
    elif opcion == "3":
        import editar_deudor
    elif opcion == "4":
        import eliminar_deudor5

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "6":
        break

    if opcion != "5":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("El resultado de la suma es:", sumar(num1, num2))
        elif opcion == "2":
            print("El resultado de la resta es:", restar(num1, num2))
        elif opcion == "3":
            print("El resultado de la multiplicación es:", multiplicar(num1, num2))
        elif opcion == "4":
            print("El resultado de la división es:", dividir(num1, num2))
        else:
            print("Opción inválida")
    if opcion == "5":
        consultar_deudores()
        print("  ")

