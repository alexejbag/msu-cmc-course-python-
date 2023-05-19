# Написать класс Nuts, экземпляры которого:
# * можно конструировать из чего угодно (в т. ч. из ничего)
# * можно индексировать по чему угодно (возвращается объект, который использовался в индексе)
# * в том числе позволяют присваивать и удалять по индексу (ничего не происходит)
# * содержат любое поле (возвращается имя этого поля)
# * в том числе позволяют присваивать и удалять поля (ничего не происходит)
# * итерируемы (последовательность пуста)
# * в виде строки представляются как "Nuts"

class Nuts:
    def __init__(self, *args):
        self.val = "Nuts"

    def __str__(self):
        return "Nuts"

    def __getitem__(self, val):
        return val

    def __getattr__(self, val):
        return val

    def __setitem__(self, val, value):
        pass

    def __setattr__(self, val, value):
        pass

    def __delitem__(self, val):
        pass

    def __delattr__(self, val):
        pass

    def __iter__(self):
        return iter(tuple())


# M, N = Nuts(), Nuts(1, 2, 3, 4)
# print(M, N)
# M[100] = N.qwerty = 42
# print(M[100], N.qwerty)
# print(*list(Nuts("QWERQWERQWER")))
# del M["QQ"], N[6:10], M[...], N._
# print(M.asdfg, N[-2])

# Nm = map(Nuts, range(10))
# print(*(f"{n}" for n in Nm))
# Nm = map(Nuts, range(10))
# print(*map(list, (map(str, N) for N in Nm)))
# N=Nuts(int)
# print(type(N))
# print(Nuts)
# print(Nuts()[Nuts()[Nuts()[Nuts()]]])
