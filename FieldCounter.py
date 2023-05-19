# Написать функцию,Stat() которая умеет выполнять две роли:
# 1)
# С одним параметром Stat(класс) — работает как декоратор класса, добавляет в объекты класса сбор статистики
# по всем полям данных, упомянутым в самом классе (т. е. встречающимся в vars(класс)), имя которых не начинается с "_"
# По всем остальным атрибутам (методам, спецметодам и т. п., а так же атрибутам, динамически добавленным в __init__()
# статистика не ведётся
# 2)
# С двумя параметрами Stat(объект, "поле") — выводит статистику использования поля поле:
# * два целых числа (количество чтений, количество записей)
# * объект — экземпляр класса, декорированного с помощью Stat
# * поле — поле этого класса
# Экземпляр класса инициализируется с помощью __init__(), т. е. класс не является потомком встроенного класса,
# не переопределяет __new__(), __getattribute__() и т. п., изначально не содержит слотов/дескрипторов.

def Stat(cls, stat_field=None):
    if stat_field:
        if "__field" in dir(cls):
            if stat_field in cls.__field:
                return cls.__field[stat_field][0], cls.__field[stat_field][1]
        return 0, 0

    if not stat_field:
        lst = []
        for key, i in vars(cls).items():
            if not callable(getattr(cls, key)) and key.find("_") != 0:
                lst.append((key, [0, 0, i]))
        cls.__field = dict(lst)

        def dec(_):
            def new_init(self, *args):
                lst = []
                for key, i in self.__field.items():
                    lst.append((key, i.copy()))
                self.__field = dict(lst)
                self.__field_init(*args)

            return new_init

        cls.__field_init = cls.__init__
        cls.__init__ = dec(cls.__init__)

        class ModifiedMethods:
            def __get__(self, obj, t=None):
                getattr(obj, "__field")[self.arg][0] += 1
                return getattr(obj, "__field")[self.arg][2]

            def __set__(self, obj, val):
                getattr(obj, "__field")[self.arg][2] = val
                getattr(obj, "__field")[self.arg][1] += 1

            def __init__(self, arg):
                self.arg = arg

        for i in cls.__field.keys():
            setattr(cls, i, ModifiedMethods(i))
    return cls
