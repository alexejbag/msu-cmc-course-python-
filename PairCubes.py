# Ввести натуральное число и проверить, представимо ли оно в виде суммы кубов двух натуральных чисел.
# Вывести YES или NO. Придумать алгоритм поэффективнее.

from math import*
s = "NO"
a = int(input())
a_new = floor(a**(1/3.0))
for i in range(a_new):
    f = a-(i**3)
    f = f**(1/3.0)
    f_new = ceil(f)
    for j in range(f_new + 1):
        if (i**3) + (j**3) == a:
            s = "YES"
            print(i, j)
            break
    if s == "YES":
        break
print(s)
