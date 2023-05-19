# Ввести в столбик последовательность целых (положительных и отрицательных) чисел, не равных нулю;
# в конце этой последовательности стоит "0". Вывести наибольшую сумму последовательно идущих элементов этой
# последовательности (не менее одного)

a = []
b = 1
i = -1
t = 0
sum = 0
maxsum = 0
while b != 0:
    i += 1
    a.append(int(input()))
    b = a[i]
for j in range(i):
    if a[j] > 0:
        t = 1
min = a[0]
for j in range(i):
    sum += a[j]
    if maxsum < sum:
        maxsum = sum
    elif sum < 0:
        sum = 0
if t == 0:
    for j in range(i-1):
        if a[j] > min:
            min = a[j]
    maxsum = min
print(maxsum)