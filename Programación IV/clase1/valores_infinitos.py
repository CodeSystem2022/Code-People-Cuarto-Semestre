import math
from decimal import Decimal


#manejos de valores infinitos
infinitos_positivos = float('inf')
print(f'infinitos positivos: {infinitos_positivos}')
print(f'Es infinito: {math.isinf(infinitos_positivos)}')

infinitos_negativos = float('-inf')
print(f'infinito negativo: {infinitos_negativos}')
print(f'Es infinito: {math.isinf(infinitos_negativos)}')

#Modulo math
infinitos_positivos = math.inf
print(f'infinitos positivos: {infinitos_positivos}')
print(f'Es infinito: {math.isinf(infinitos_positivos)}')

infinitos_negativos = -math.inf
print(f'infinito negativo: {infinitos_negativos}')
print(f'Es infinito: {math.isinf(infinitos_negativos)}')

#Modulo decimal
infinitos_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinitos_positivo}')
print(f'infinito positivo: {math.isinf(infinitos_positivo)}')

infinitos_negativo = Decimal('-Infinity')
print(f'Infinito negativo: {infinitos_negativo}')
print(f'infinito negativo: {math.isinf(infinitos_negativo)}')