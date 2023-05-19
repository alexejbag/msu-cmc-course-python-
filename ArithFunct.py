# Написать четыре функции (функционала): ADD(f, g), SUB(f, g), MUL(f, g) и DIV(f, g), параметрами которых могут быть
# как обычные объекты, так и функции от одной переменной (проверить, является ли объект функцией можно с помощью
# callable(объект)). Возвращать эти функционалы должны функцию от одной переменнойh(x), которая выполняет
# соответствующее действие (f(x)+g(x), f(x)-g(x), f(x)*g(x) и f(x)/g(x)) над этими переменными.
# Если f или g не были функцией, вместо f(x) используется f,
# а вместо g(x) — g (например, при умножении функции на константу).

from math import*


def ADD(f, g):
    if callable(f) and callable(g):
        def h(x):
            return f(x) + g(x)
        return h

    if callable(f):
        def h(x):
            return f(x) + g
        return h

    if callable(g):
        def h(x):
            return f + g(x)
        return h

    def h(x):
        return f + g
    return h


def SUB(f, g):
    if callable(f) and callable(g):
        def h(x):
            return f(x) - g(x)
        return h

    if callable(f):
        def h(x):
            return f(x) - g
        return h

    if callable(g):
        def h(x):
            return f - g(x)
        return h

    def h(x):
        return f - g
    return h


def MUL(f, g):
    if callable(f) and callable(g):
        def h(x):
            return f(x) * g(x)
        return h

    if callable(f):
        def h(x):
            return f(x) * g
        return h

    if callable(g):
        def h(x):
            return f * g(x)
        return h

    def h(x):
        return f * g
    return h


def DIV(f, g):
    if callable(f) and callable(g):
        def h(x):
            return f(x) / g(x)
        return h

    if callable(f):
        def h(x):
            return f(x) / g
        return h

    if callable(g):
        def h(x):
            return f / g(x)
        return h

    def h(x):
        return f / g
    return h

