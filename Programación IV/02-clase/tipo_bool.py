
# Bool contiene valores de True Y False
# Los tipos Numericos, es el false para el = (cero), true para los demas valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')



valor = 15
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')


# Tipo string -> false '', True demas valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

valor = 'hola'
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

# Tipo colecciones -> False para colecciones vacias
# Tipo colecciones -> True para todas las demas colecciones
# Lista
valor = []
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

valor = [2,3,4]
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')


valor = (5,)
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

# Diccionario

valor = {}
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

# Sentencias de control con bool
if '':# se puede usar cualquiere de las comprobaciones de arriba
    print('Regresa verdadero')
else:
    print('Regresa falso')


# ciclos
variable = 17# se puede usar cualquiere de las comprobaciones de arriba
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')


