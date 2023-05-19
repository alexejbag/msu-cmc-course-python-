# Вводится ASCII-art с изображением стакана (возможно, с водой), падающего в ведро (последняя строка — пустая).
# Толщина стенок стакана — 1. После падения стакан оказывается на боку в левом нижнем углу ведра (даже если он
# размером с ведро; больше он не бывает), а вода из него выливается, заполняя ровным слоем дно ведра и заслоняя
# стакан (толщина слоя округляется в большую сторону). Вывести ведро с упавшим стаканом.

from math import*
a = []
result = []
x = y = water = 0
s = input()
n = len(s)  # дно ведра
while s:
    a.append(s)
    s = input()
for j in a:
    if j.count('#'):
        y += 1  # дно стенка стакана
        x = j.count('#')  # дно стакана
    water += j.count('*')

water_layer_amount = ceil(water/n)
empty_layer = "." * n,
water_layer = "*" * n
glass_wall = "#" * y + "." * (n - y)
glass_bottom = "#" + "." * (n - 1)

result = a.copy()
m = len(a)  # стенка ведра
for j in range(m-x, m):
    if j == m-1 or j == m-x:
        result[j] = glass_wall
        continue
    result[j] = glass_bottom
for j in range(0, m-x):
    result[j] = empty_layer
for j in range(m-water_layer_amount, m):
    result[j] = water_layer

for j in result:
    print(j)
