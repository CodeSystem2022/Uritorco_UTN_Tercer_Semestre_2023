
archivo = open('prueba.txt', 'r',
               encoding='utf8') # las letras son: 'r' read, 'a' append, 'w' write, 'x'
# print(archivo.read())
# print(archivo.read(15))
# print(archivo.read(10)) # Continuamos desde la línea anterior
# print(archivo.readline())
# print(archivo.readline())

# vamos a iterar el archivo, cada una de las líneas
# for linea in archivo:
    # print(linea): iteramos todos los elementos del archivo
# print(archivo.readlines()[11]) # accedemos al archivo como si estuviera en una lista
# Anexamos información, coipiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()# cerramos el primer archivo
archivo2.close()# cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')



