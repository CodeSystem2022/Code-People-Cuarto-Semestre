
# help(str.join)
#  Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
tupla_str = ('hola', 'alumnos', 'tecnicatura', 'Universitaria')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = { 'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'llaves: {llaves}, Type: {type(llaves)}')
print(f'valores: {valores}, Type: {type(valores)}')
