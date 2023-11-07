import math
from decimal import Decimal
# NaN (Not a NUmber)


a = float('NaN')
print(f'a: {a}')

#Modulo Math
a = float('NaN')
print(f'Es de tipo NaN(Not a NUmber)?: {math.isnan(a)}')
a = float('2.0')
print(f'Es de tipo NaN(Not a NUmber)?: {math.isnan(a)}')

#Modulo  DECIMAL
a = Decimal('NaN')
print(f'Es de tipo NaN(Not a NUmber)?: {math.isnan(a)}')
a = Decimal('2.0')
print(f'Es de tipo NaN(Not a NUmber)?: {math.isnan(a)}')



