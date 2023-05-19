# Известно, что любое натуральное число можно представить в виде суммы не более чем четырех квадратов неотрицательных
# целых чисел (теорема Лагранжа). Ввести натуральное N⩽100000 и найти для него такие целые неотрицательные x,y,z и t,
# чтобы x²+y²+z²+t²=N. Вывести все такие четвёрки в следующем формате: x,y,z и t — через пробел, и упорядочены по
# убыванию, а сами четвёрки — лексикографически по возрастанию (без повторений).

from math import*

N = int(input())
x = y = z = t = 0
x_1 = ceil(sqrt(N/4))
x_2 = floor(sqrt(N))
for i_x in range(x_1, x_2 + 1):
    y_1 = ceil(sqrt((N - i_x**2) / 3))
    y_2 = floor(sqrt(N - i_x**2))
    for i_y in range(y_1, y_2 + 1):
        z_1 = ceil(sqrt(((N - i_x**2) - i_y**2) / 2))
        z_2 = floor(sqrt((N - i_x**2) - i_y**2))
        for i_z in range(z_1, z_2 + 1):
            i_t = N_new = N - (i_x**2 + i_y**2 + i_z**2)
            i_t = ceil(sqrt(i_t))
            if i_t**2 == N_new and i_x >= i_y >= i_z >= i_t:
                print(i_x, i_y, i_z, i_t)