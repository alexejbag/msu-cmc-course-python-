# Вводится две строки: произвольная функция над x, содержащая арифметические операции, имеющая единственный корень
# на интервале (-1.5, 1.5), непрерывная на нём и принимающая значения разных знаков на концах интервала,
# и натуральное число D. Вывести корень данной функции с точностью ровно D знаков после запятой (нули тоже выводятся).
# Воспользоваться десятичным контекстом для задания точности (см. примеры выше на странице документации).

from math import*
import decimal
from decimal import *

s = input()
d = int(input())
getcontext().prec = d + 2
eps = decimal.Decimal(0.1) / (10**(d-1))
a, b = decimal.Decimal(-1.5), decimal.Decimal(1.5)
x = decimal.Decimal((a + b) / 2)
y = eval(s)

while fabs(y) > eps:
    if y > 0:
        b = decimal.Decimal(x)
    else:
        a = decimal.Decimal(x)
    x = decimal.Decimal((a + b) / 2)
    y = eval(s)
if fabs(x) == 0:
    template = '{:.' + str(d) + 'f}'
    print(template.format(x))
elif fabs(x) < 1 and x < 0:
    x1 = str(x)[0:-2]
    print(x.quantize(Decimal(x1), ROUND_HALF_UP))
else:
    x1 = str(x)[0:-1]
    print(x.quantize(Decimal(x1), ROUND_HALF_UP))
