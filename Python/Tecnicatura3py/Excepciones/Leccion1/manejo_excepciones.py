#Un error o una excepcion es cuando un programa acaba de manera abrupta o lanza un error y no se termina de ejecutar
#La clase padre de todas las excepcones es BaseException-Exception. A partir de estas excepciones se producen las clases hijas 
from NumerosIgualesException import NumerosIgualesException
resultado = None
try:
  a= int(input('Digite el primer numero: '))
  b=int(input('Digite el primer numero: '))
  if a ==b:
      raise NumerosIgualesException('Son numeros iguales') #Raise nos permite arrojar excepciones
  resultado=a/b #modificamos
except TypeError as e:
    print(f'TypeError-Ocurrio un error:{type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError -Ocurrió un error:{type(e)}')
except Exception as e:
    print (f'Exception-Ocurrio un error:{type(e)}') 
else:
    print("No se arrojo una excepcion")
finally:
    print("Ejecucion de este bloque finally")
print(f'El resultado es: {resultado}')
print('seguimos...')

