import math
from decimal import Decimal
# Manejo de valores infinitos
#infinitos_positivo = float('inf')
#print(f'Infinito positivo: {infinitos_positivo}')
#print(f'Es infinito: {math.isinf(infinitos_positivo)}')

#infinitos_negativo = float('-inf')
#print(f'Infinito negativo: {infinitos_negativo}')
#print(f'Es infinito: {math.isinf(infinitos_negativo)}')

# Modulo Math
#infinitos_positivo = math.inf
#print(f'Infinito positivo: {infinitos_positivo}')
#print(f'Es infinito: {math.isinf(infinitos_positivo)}')

#infinitos_negativo = -math.inf
#print(f'Infinito negativo: {infinitos_negativo}')
#print(f'Es infinito: {math.isinf(infinitos_negativo)}')

# Modulo decimal

infinitos_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinitos_positivo}')
print(f'Es infinito: {math.isinf(infinitos_positivo)}')

infinitos_negativo = Decimal('-Infinity')
print(f'Infinito negativo: {infinitos_negativo}')
print(f'Es infinito: {math.isinf(infinitos_negativo)}')