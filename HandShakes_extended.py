# Вводить построчно разделённые запятыми последовательности натуральных чисел (кортежи), окончание ввода: пустая строка.
# Числа в строке — идентификаторы людей, которые познакомились (или уже были знакомы) на некоторой вечеринке.
# Верно ли, что от любого из перечисленных людей можно построить цепочку знакомств к любому другому?
# Иными словами, если считать каждую пару x,y ребром неориентированного графа, является ли этот граф связным?
# Вывести YES или NO.

result = "NO"
flag = 1
counter = 0
people = t1 = set()
my_list = []
s = input()
if s:
    t1 = set(eval(s))
    people |= t1
    print(t1)
    s = input()
while s:
    t2 = set(eval(s))
    people |= t2
    print(t2)

    if t1 & t2:
        for i in t2:
            t1.add(i)
    else:
        my_list.append(tuple(t2))

    print("Result:", t1, type(t1), sep=":")
    s = input()
print("my_list: ", my_list)
while flag:
    counter = 0
    for i in my_list:
        print("now check", i)
        for j in i:
            print("now check in i: ", j)
            if j in t1:
                t1 |= set(i)
                my_list.remove(i)
                print("my_list после удаления эл-та: ", my_list)
                counter += 1
                break
    if counter == 0:
        flag = 0
        break

if t1 == people and t1:
    result = "YES"
print("группа знакомых: ", t1)
print("all people at party: ", people)
print(result)
