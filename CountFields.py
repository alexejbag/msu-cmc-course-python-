# Написать функцию fcounter(), которая первым параметром получает некоторый класс, а остальные параметры применяет
# для создания экземпляра этого класса. Функция должна возвращать 4 отсортированных списка: имена методов класса,
# имена полей класса, имена методов, которые появились в экземпляре (т. е. в классе их не было, а при создании
# экземпляра они появились) и имена полей, которые появились в экземпляре (под «полями» имеются в виду не-callable()
# атрибуты). Внимание! Поле может внезапно сделаться классом (и наоборот), такие ситуации тоже надо отслеживать.

def fcounter(C, *args):
    tpl = []
    tmp = []
    c = C(*args)
    # 1
    method_list = [func for func in dir(C) if callable(getattr(C, func))]
    field_list = [field for field in dir(C) if not callable(getattr(C, field))]
    for i in method_list:
        if "__" not in i and i[0] != '_':
            tmp.append(i)
    tpl.append(sorted(tmp))
    tmp = []
    # 2
    for i in field_list:
        if "__" not in i and i[0] != '_':
            tmp.append(i)
    tpl.append(sorted(tmp))
    tmp = []
    # 3
    for i, j in dict.items(c.__dict__):
        if "function" in str(j) and i not in tpl[0] and i[0] != '_':
            tmp.append(i)
    tpl.append(sorted(tmp))
    tmp = []
    # 4
    for i, j in dict.items(c.__dict__):
        if "function" not in str(j) and i not in tpl[1] and i[0] != '_':
            tmp.append(i)
    tpl.append(sorted(tmp))
    tmp = []

    return tpl
