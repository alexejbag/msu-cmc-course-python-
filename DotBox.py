# Вводить вещественные числа x, y и z по три в строке через запятую, считая их координатами точек
# (не менее одной тройки). Конец ввода — пустая строка. Вывести минимальный объём параллелепипеда со сторонами,
# параллельными осям координат, содержащего все точки.

s = input()
x, y, z = eval(s)
x_min = x_max = x
y_min = y_max = y
z_min = z_max = z
while s:
    x, y, z = eval(s)
    if x < x_min:
        x_min = x
    elif x > x_max:
        x_max = x
    if y < y_min:
        y_min = y
    elif y > y_max:
        y_max = y
    if z < z_min:
        z_min = z
    elif z > z_max:
        z_max = z
    s = input()

x_max -= x_min
y_max -= y_min
z_max -= z_min
print(x_max * y_max * z_max)