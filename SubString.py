# Реализовать класс SubString, который бы полностью воспроизводил поведение str,
# но вдобавок бы поддерживал операцию вычитания строк.
# Вычитание устроено так: «уменьшаемое» просматривается посимвольно,
# и если соответствующий символ присутствует в «вычитаемом», то он однократно удаляется из обеих строк.
# К моменту прохождения теста ничего нового, кроме класса SubString в глобальном пространстве имён быть не должно

from collections import UserString

class SubString(UserString):
    def __sub__(self, other):
        import collections
        other = collections.Counter(other)
        # print(">>>", other)
        result = []
        for c in self:
            if other[c] != 0:
                other -= collections.Counter(c)
            else:
                result.append(str(c))
        result = "".join(result)
        return SubString(result)

del UserString

#1
import string
S = SubString("NOTE: gravity is a myth, the Earth sucks.")
print(S-string.ascii_lowercase)
print(string.digits+S-string.ascii_uppercase)
#2
S = SubString("NOTE: gravity is a myth, the Earth sucks.")
for m in ("isprintable", "upper", "title", "swapcase", "capitalize", "isascii"):
    print(getattr(S, m)())


# class SubString(str):
#
#     def __add__(self, arg):
#         print("****")
#         ret = super().__add__(arg)
#         if isinstance(ret, str):
#             return SubString(ret)
#         else:
#             return ret
#
#     def __mul__(self, arg):
#         ret = super().__mul__(arg)
#         if isinstance(ret, str):
#             return SubString(ret)
#         else:
#             return ret
#
#     def __getitem__(self, item):
#         ret = super().__getitem__(item)
#         if isinstance(ret, str):
#             return SubString(ret)
#         else:
#             return ret
#
#     def replace(self, smth1, smth2):
#         ret = super().replace(smth1, smth2)
#         if isinstance(ret, str):
#             return SubString(ret)
#         else:
#             return ret
#
#     def __sub__(self, other):
#         lst1, lst2 = list(self), list(other)
#         for char in lst2:
#             if char in lst1:
#                 lst1.remove(char)
#         result = "".join(lst1)
#         return SubString(result)
