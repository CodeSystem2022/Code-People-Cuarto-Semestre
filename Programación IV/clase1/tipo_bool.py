
# Bool contiene los valores de True y False
# los tipos númericos, es false para el 0 (cero) , true para los demas valores
valor = 0.0
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

#tipo str -> False '', True para los demas valores
valor = ''
resultado = bool(valor)
print(f'valor:{valor} resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor:{valor} resultado: {resultado}')

#Tipo colecciones -> false para colecciones vacias
#Tipo colecciones -> true para todas  las demas
#Lista
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia:{valor} resultado: {resultado}')

valor = [2,3,4]
resultado = bool(valor)
print(f'valor de una lista con elementos:{valor} resultado: {resultado}')

#Tupla
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia:{valor} resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'valor de una tupla con elementos:{valor} resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio:{valor} resultado: {resultado}')

valor = {'nombre': 'Luis', 'apellido': 'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario con elementos:{valor} resultado: {resultado}')

#Sentencias de control con Bool
if bool(''):
    print('Regresa verdadero')
else:
    print('Regresa falso')

if bool('1 : 12'):
    print('Regresa verdadero')
else:
    print('Regresa falso')

#Ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')