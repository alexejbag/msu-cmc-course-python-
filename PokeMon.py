# Участники некоторой карточной игры владеют несколькими колодами, из которых они составляют свой уникальный игровой
# набор. Каждая колода имеет номер; колоды с одинаковыми номерами содержат совпадающие наборы карт.
# Ввести строки вида "имя игрока / номер колоды" (колода принадлежит игроку) или "номер колоды / название карты"
# (карта входит в колоду); последняя строка пустая. Вывести в алфавитном порядке имена игроков, которые могут составить
# игровой набор из наибольшего числа различных карт.

from collections import *
owners = defaultdict(list)
cards = defaultdict(list)
d = dict()
res = []
s = input()
while s:
    temp = s.split(' / ')
    if len(temp[0].split(' ')) == 2:
        owners[temp[0]].append(temp[1])
    elif '0' <= temp[1] <= '9':
        owners[temp[0]].append(temp[1])
    else:
        cards[temp[0]].append(temp[1])
    s = input()

for k in owners:
    tmp = []
    for j in owners[k]:
        tmp += cards[j]
    owners[k] = len(set(tmp))

n = 0
for k in owners.values():
    n = k if n < k else n
for k in owners:
    if owners[k] == n:
        res.append(k)
res.sort()
for j in res:
    print(j)
