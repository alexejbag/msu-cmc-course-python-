# Написать бесконечный генератор PiGen(), вычисляющий Decimal представление числа Пи c 9999 знаками после запятой
# (всего 10000☺) по алгоритму Чудновских. На каждой итерации PiGen() возвращает значение для очередного k

from itertools import*
from math import*
from decimal import *
given_prec = 10000
getcontext().prec = given_prec


def PiGen():
    const = (Decimal(640320 ** 3).sqrt()) / 12
    k = s = Decimal(0)
    for _ in count():
        s += ((factorial(6*k) * (545140134 * k + 13591409)) /
              (factorial(3*k) * ((factorial(k))**3) * ((-262537412640768000) ** k)))
        k += 1
        res = const / Decimal(s)
        yield res
