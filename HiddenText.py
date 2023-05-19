# Ввести две строки и проверить, содержится ли вторая в первой, с учётом того, что символы второй строки могут
# находиться в первой на некотором равном расстоянии друг от друга. Вывести YES или NO.

from math import*
b = 0
str1 = input()
str2 = input()
l1 = len(str1)
l2 = len(str2)
if l2 == 2:
    n = l1
else:
    n = ceil(l1 / l2) + 1
for j in range(1, n):
    for i in range(j):
        if str2 in str1[i::j]:
            b = 1
            break
    if b == 1:
        break
if b:
    print("YES")
else:
    print("NO")
