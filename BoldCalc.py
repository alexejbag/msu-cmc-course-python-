# Написать программу — калькулятор с переменными и обработкой ошибок. Программа построчно вводит команды калькулятора,
# и если надо, выводит результат их выполнения или ошибку.
# * пробелы в строках игнорируются
# * команда, начинающаяся на '#' — комментарий, такие команды игнорируются
# * команда вида "Идентификатор = выражение" задаёт переменную Идентификатор (именование как в Python)
# * если слева от "=" стоит не идентификатор, выводится "Assignment error"; всё, что справа, игнорируется
# * команда вида "выражение" выводит значение выражения.
# * выражение — это арифметическое выражение, состоящее из
#       целых чисел
#       уже определённых идентификаторов
#       круглых скобок
#       действий +, -, *, /, % и унарных + и -
#       деление целочисленное
# * любое другое выражение приводит к выводу ошибки "Syntax error"
# * если выражение нельзя вычислить, потому что в нём встречаются неопределённые переменные, выводится ошибка "Name error"

import re
flag = 0
regex = "((?P<variable>[\w]+) ?= ?)? ?(?P<example>[+\*%-]*(([)(])?(([\d]+)|[A-Za-z_][\w]*)[=+\/*%\(\)-]*)+)"
s = input()
while s:
    flag = 0
    s = s.replace(' ', '')
    if s.find('#') == 0:
        s = input()
        continue
    try:
        s = re.sub("(?P<na>[A-Za-z_][\w]*)", "\g<na>_variable", s)
        if re.findall("(//)|(\*\*)|([\w]+\()|(\d\()|([\w]+ ?= ?\d+\.\d+)", s):
            raise SyntaxError
        e = re.match(regex, s)  # not re.search
        # print(e)
        variable = e.group("variable")
        e = re.match(regex, s)
        # print(e)
        example = e.group("example")
        if variable and not variable.isidentifier():  # keyword.iskeyword() ?!
            raise AttributeError
        if s.find('/0') == -1:
            flag = 1
            exec(s)
        if '=' not in s:
            s = s.replace('/', '//')
            if s.find('/0') == -1:
                flag = 1
                print(eval(s))

    except AttributeError:
        flag = 1
        print("Assignment error")

    except NameError:
        flag = 1
        print('Name error')

    except SyntaxError:
        flag = 1
        print('Syntax error')

    except TypeError:
        flag = 1
        print('Syntax error')

    if flag == 0:
        print('Runtime error')

    s = input()
