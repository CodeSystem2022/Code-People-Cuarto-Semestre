import math
from decimal import Decimal

# NaN (Not a number)
a = float('NaN')
print(f'a: {a}')

#Modulo math
a = float('nan')
#a = float('2.0')
print(f'Es un tipo NaN(Not a Number)?: {math.isnan(a)}')

#Modulo decimal
a = Decimal('nan')
print(f'Es un tipo NaN(Not a Number)?: {math.isnan(a)}')