# Написать программу, которой на вход подаётся синтаксически верное регулярное выражение, а затем — строки поиска
# (последняя строка пустая). Программа должна выводить информацию о первой найденной в строке поиска подстроке,
# соответствующей регулярному выражению, в таком формате:
# * если подстрока не найдена, выводится «<NONE>»
# * если подстрока найдена, выводится позиция: подстрока, где «позиция» — это номер символа в строке, начиная с которого была найдена подстрока
# * если в регулярном выражении присутствовала группировка с сохранением (попросту скобочки), выводится номер группы/позиция: подстрока для каждой группы
# * если в регулярном выражении присутствовали именованные группы, выводится имя группы/позиция: подстрока для каждой группы
# * если какая-то группа присутствует в исходном выражении, но не нашла сопоставления (например, была помечена повторителем * и пропущена), она не выводится

import re
rv = input()
s = input()

e = re.findall("\(([^)]*)\)", rv)
# e = re.findall("<([^>]*)", rv)
namedgroups = [[]]
for j in e:
    tmp = re.findall("<([^>]*)", j)
    namedgroups.append(tmp)

while s:
    f = 0
    matches = re.finditer(rv, s, re.MULTILINE)
    for match in matches:
        f += 1
        print("{start}: {match}".format(start=match.start(), match=match.group()))

        for i in range(len(match.groups())):
            i += 1
            if not match.group(i):
                continue

            print("{groupNum}/{start}: {group}".format(groupNum=i, start=match.start(i), group=match.group(i)))

        for i, j in enumerate(namedgroups):
            if j and match.group(i):
                print("{namegroup}/{start}: {group}".format(namegroup=namedgroups[i][0], start=match.start(i), group=match.group(i)))

    if not f:
        print('<NONE>')

    s = input()
