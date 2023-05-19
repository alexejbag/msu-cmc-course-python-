# Написать генератор YinYang(Seq,,1,,, …, Seq,,n,, …), которая получает на вход конечное количество
# (возможно, бесконечных) числовых последовательностей, а возвращает сначала все чётные элементы этих
# последовательностей, а затем нечётные. Например, YinYang([1,2,3], [6,5,4,3]) вернёт 2 … 6 … 4 … 1 … 3 … 5 … 3.

from itertools import*
def YinYang(*seq):
    # 1)
    # I = list(chain(seq, seq))
    # ll = len(I) // 2
    # i1 = I[:ll]
    # i2 = I[ll:]

    # 2)
    # i1, i2 = tee(seq, 2)

    # 3)
    i1, i2 = zip(*(tee(s, 2) for s in seq))
    for j in list(i1):
        for elem in j:
            if not(elem % 2):
                yield elem
    for j in list(i2):
        for elem in j:
            if elem % 2:
                yield elem

    # 4)
    # i1, i2 = zip(*(tee(s, 2) for s in seq))
    # yield from (elem for elem in chain.from_iterable(i1) if not (elem % 2))
    # yield from (elem for elem in chain.from_iterable(i2) if (elem % 2))
