# Ввести построчно список участников некоторого соревнования на скорость неизвестно чего в виде:
# "Имя Фамилия Название команды часы:минуты:секунды" (последняя строка пустая), и вывести всех, кто занял
# первые три места (минимальное затраченное неизвестно на что время; одно место может занять несколько человек,
# если время совпадает), в порядке возрастания времени, а внутри одного времени — лекcикографически:
# "фамилия, имя, команда".
# Дополнительное условие: таблица чемпионов должна быть аккуратной: поля «Имя», «Фамилия», «Название команды» и «Время»
# должны начинаться в одной колонке, но при этом быть максимально «упакованными»:
# столбцы в таблице должны быть разделены ровно одним пробелом.

from operator import itemgetter
champ = []
a = []
s = input()
while s:
    temp = s.split(' ')
    time = str(temp[-1])
    temp.pop()
    team = ""
    for j in temp[2:]:
        team += str(j) + " "
        temp.pop()
    team = team[:-1]
    temp.append(team)
    temp.append(str(time))
    time = time.split(':')
    for i, j in enumerate(time):
        time[i] = int(j)
    temp += time
    a.append(temp)
    s = input()

a = sorted(a, key=itemgetter(4, 5, 6, 1, 0, 2))
for j in a:
    del j[-3:]

name0 = name1 = name2 = name3 = 0
j = 0
n = len(a)
for i in range(3):
    if j == n:
        break
    check = a[j][-1]
    while check:
        if j == n:
            break
        if check != a[j][-1]:
            break
        champ.append(a[j])
        if len(a[j][0]) > name0:
            name0 = len(a[j][0])
        if len(a[j][1]) > name1:
            name1 = len(a[j][1])
        if len(a[j][2]) > name2:
            name2 = len(a[j][2])
        if len(a[j][3]) > name3:
            name3 = len(a[j][3])
        j += 1

fmt0 = "{0:"+str(name0+1)+"}"
fmt1 = "{0:"+str(name1+1)+"}"
fmt2 = "{0:"+str(name2+1)+"}"
fmt3 = "{0:"+str(name3)+"}"
for j in champ:
    print(fmt0.format(j[0]), end="")
    print(fmt1.format(j[1]), end="")
    print(fmt2.format(j[2]), end="")
    print(fmt3.format(j[3]))
