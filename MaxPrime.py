# Ввести натуральное 1000000000000>N>1 и вывести максимальное простое число, не превосходящее N.

from math import*
a = int(input())
if (a % 2 == 0) and (a != 2):
    a = a - 1
x = a

for i in range(0, a, 2):
    flag = 0
    x = a - i
    c = ceil(sqrt(x))
    for j in range(3, c, 2):
        if x % j == 0:
            flag = 1
            break
    if flag == 0:
        break
print(x)


# не подходит для больших N!
# following attempt leads to Memory Error for large value of N
# import math
# def primes(N):
#     """Возвращает все простые числа от 2 до N"""
#     sieve = set(range(2, N+1))  # мн-во, содержащее все натуральные чисал от 2 до N
#     for i in range(2, math.ceil(math.sqrt(N))):
#         if i in sieve:
#             sieve -= set(range(2 * i, N+1, i))
#     return sieve
# print(help(primes))
# print(primes(91000))


# following attempt leads to Memory Error for large value of a
# sieve = list(range(a+1))
# print(sieve)
# for i in range(a+1):
#     sieve[i] = 0
# print(sieve)
# i = 2
# while (i*i < a):
#     if (sieve[i] == 0):
#         k = i*i
#         while (k <= a):
#             sieve[k] = 1
#             k += i
#     i += 1
# print(sieve)
# for i in range(a, 0, -1):
#     if (sieve[i] == 0):
#         print(i)
#         break

# n = int(input())
# for num in range(2, n):
#     prime = True
#     #c = ceil(sqrt(num))
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#        print(num)
