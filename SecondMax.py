# Ввести по одному в строке целые числа (не менее одного, конец ввода "0"), вывести второй максимум последовательности
# (число, строго меньшее максимума последовательности, и не меньшее остальных чисел в ней), и "NO", если такового нет.

first = second = 0
a = int(input())
while a != 0:
    if a > first or first == 0:
        second = first
        first = a
    elif first > a > second:
        second = a
    a = int(input())

if second == 0:
    print("NO")
else:
    print(second)

# # old solution:
# b = flag = 1
# second_max = 0.1
# a = int(input())
# max = a
# if a == 0:
#     b = 0
#     flag = 0
#
# if b != 0:
#     a = int(input())
#     if a == 0:
#         b = 0
#         flag = 0
#     elif a > max:
#         second_max = max
#         max = a
#     elif a == max:
#         max = a
#     elif a < max:
#         second_max = a
#
# if b != 0:
#     a = int(input())
#
# while a != 0:
#     if a > max:
#         second_max = max
#         max = a
#     elif a == max:
#         max = a
#     elif (a < max) and ((a > second_max) or (second_max == 0.1)):
#         second_max = a
#     a = int(input())
#
# if flag == 0:
#     print("NO")
# elif max == second_max:
#     print("NO")
# elif second_max == 0.1:
#     print("NO")
# else:
#     print(second_max)
