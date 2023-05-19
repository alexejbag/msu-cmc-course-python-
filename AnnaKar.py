# Ввести два натуральных числа через запятую: N и W, а за ними построчно некоторый текст. Последняя строка — пустая.
# Выделить из текста слова (последовательности символов, для которых isalpha() истинно), преобразовать их в нижний
# регистр, и вывести Top-N по частоте встречаемости слов длиной не меньше W.
# Например, в Top-2 список входят все слова, которые встречаются чаще всех, и все слова, которые встречаются реже этих,
# но чаще всех остальных (обратите внимание на то, что Counter.most_common() ведёт себя иначе).
# Ключи сортировки вывода: сначала длина, потом слово. Если различных количеств встречаемых слов не больше N
# (например, все слова в тексте встречаются по разу), в Top-N входят все слова.


from collections import*
from operator import itemgetter
s = input()
N, W = eval(s)
D = defaultdict(int)
D_res = dict()
set_values = set()
res = []
while s:
    s = s.replace(';', '')
    s = s.replace('.', '')
    s = s.replace(':', '')
    s = s.replace(',', '')
    s = s.replace("'", ' ')
    s = s.replace('"', '')
    s = s.replace("-", ' ')
    temp_list = s.split(' ')
    for j in temp_list:
        if len(j) >= W:
            if j.isalpha():
                D[j.lower()] += 1
            if j[0:-1].isalpha() and not j.isalpha():
                D[j[0:-1].lower()] += 1
            if j[0:-2].isalpha() and not j[0:-1].isalpha():
                D[j[0:-2].lower()] += 1
            if j[1:].isalpha() and not j.isalpha():
                D[j[1:].lower()] += 1
    s = input()

for j in D.values():
    set_values |= {j}
list_value = list(set_values)
list_value.sort()
list_value = list_value[-N:]
for j in D.items():
    if j[1] in list_value:
        D_res.update({j[0]: j[1]})
for j in D_res:
    res.append([j, D_res[j]])
res = sorted(res, key=itemgetter(1, 0))
for j in res:
    print(j[1], end="")
    print(":", j[0])
