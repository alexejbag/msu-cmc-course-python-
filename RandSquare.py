# Написать функцию randsquare(A, B), принимающую на вход две пары вещественных чисел — координаты диагонали квадрата
# на плоскости. Функция должна возвращать случайную точку, принадлежащую этому квадрату (точка имеет право принадлежать
# границе, хотя вероятность этого события будем считать нулевой).

from random import *
from math import*


def randsquare(arg1, arg2):

    def rotation(alpha, x, y):
        if alpha > 0:
            temp_x = x
            x = x*cos(alpha) - y*sin(alpha)
            y = temp_x*sin(alpha) + y*cos(alpha)
        elif alpha < 0:
            alpha *= -1
            temp_x = x
            x = x * cos(alpha) + y * sin(alpha)
            y = -temp_x * sin(alpha) + y * cos(alpha)
        return x, y

    def check(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3):
        r1 = (x_1 - x_0) * (y_2 - y_1) - (x_2 - x_1) * (y_1 - y_0)
        r2 = (x_2 - x_0) * (y_3 - y_2) - (x_3 - x_2) * (y_2 - y_0)
        r3 = (x_3 - x_0) * (y_1 - y_3) - (x_1 - x_3) * (y_3 - y_0)
        if (r1 >= 0) and (r2 >= 0) and (r3 >= 0):
            return 1
        if (r1 <= 0) and (r2 <= 0) and (r3 <= 0):
            return 1
        return 0

    x_1, y_1 = arg1
    x_2, y_2 = arg2
    if y_2 > y_1:
        x_1, x_2 = x_2, x_1
        y_1, y_2 = y_2, y_1
    m_x = (x_1 + x_2) / 2
    m_y = (y_1 + y_2) / 2
    d = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2) / 2
    # angle = asin((x_1 - m_x)/d)
    # x_1, y_1 = rotation(angle, x_1, y_1)
    # x_2, y_2 = rotation(angle, x_2, y_2)
    # x_3, y_3 = m_x - d, m_y
    # x_4, y_4 = m_x + d, m_y
    x_3, y_3 = (x_2 + x_1) / 2 - (y_2 - y_1) / 2, (y_2 + y_1) / 2 + (x_2 - x_1) / 2
    x_4, y_4 = (x_2 + x_1) / 2 + (y_2 - y_1) / 2, (y_2 + y_1) / 2 - (x_2 - x_1) / 2
    print(x_1, y_1)
    print(x_2, y_2)
    print(x_3, y_3)
    print(x_4, y_4)
    x_1 -= x_2
    x_3 -= x_2
    x_4 -= x_2
    y_1 -= y_2
    y_3 -= y_2
    y_4 -= y_2
    r_x = random() * (x_4 + x_3) + x_2
    r_y = random() * (y_4 + y_3) + y_2
    return r_x, r_y
    # while 1:
    #     res_x = (random() * 3 * d) + m_x
    #     res_y = (random() * 3 * d) + m_y
    #     # res_x, res_y = rotation(angle, res_x, res_y)
    #     c1 = check(res_x, res_y, x_1, y_1, x_2, y_2, x_3, y_3)
    #     c2 = check(res_x, res_y, x_1, y_1, x_2, y_2, x_4, y_4)
    #     if c1 or c2:
    #         return res_x, res_y


def showgr(Dots, Corners, Name="Dots"):
    import numpy as np
    import matplotlib.pyplot as plt

    X, Y = zip(*Dots)
    fig, ax = plt.subplots(num=Name)
    ax.set_aspect(1)
    ax.scatter(X, Y)
    ax.fill(*Corners, fill=False)
    plt.show()

def show(A, B, num=1000):
    dots = [randsquare(A, B) for i in range(num)]
    R = [ (A[0], (B[0]+A[0])/2-(B[1]-A[1])/2, B[0], (B[0]+A[0])/2+(B[1]-A[1])/2),
          (A[1], (B[1]+A[1])/2+(B[0]-A[0])/2, B[1], (B[1]+A[1])/2-(B[0]-A[0])/2)]
    showgr(dots, R)

show((-9, 10), (8, 20.5), 1000)


def test_fill(A, B, num=10000):
    (x0, y0), (x1, y1) = A, B
    x2, y2 = (x1+x0)/2-(y1-y0)/2, (y1+y0)/2+(x1-x0)/2
    x3, y3 = (x1+x0)/2+(y1-y0)/2, (y1+y0)/2-(x1-x0)/2

    def sc(x, y, w=1, t=float):
        X = ((x-x0)*(y2-y0)+(y-y0)*(y3-y0))/((x3-x0)*(y2-y0)+(x0-x2)*(y3-y0))
        Y = ((x0-x)*(x2-x0)+(y0-y)*(x3-x0))/((y3-y0)*(x2-x0)+(y0-y2)*(x3-x0))
        return t(X*w), t(Y*w)
    w = int(sqrt(num)/10)
    res = {sc(*randsquare(A, B), w, int) for i in range(num)}
    if len(res) != w**2:
        print(f"Missing/extra cells in {w}x{w} grid:", *(res^{(i,j) for i in range(w) for j in range(w)}))
    return len(res) == w**2


print(test_fill((-9, 10), (8, 20.5), 1000))


# print(randsquare((-9, 10), (8, 20.5)))
