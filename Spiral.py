# Написать класс Spiral, экземпляр которого образуется из строки, содержащей одну или несколько последовательностей
# одинаковых символов, например, "122333444455555". При преобразовании в строку такая последовательность должна
# «закручиваться в спираль» против часовой стрелки(см. пример).
# Помимо преобразования в строку объект типа Spiral должен:
# * поддерживать сложение с таким же объектом: существующие в исходном объекте последовательности увеличиваются на
#       соответствующее количество символов, новые — добавляются в конец
# * поддерживать вычитание объектов типа Spiral, при этом существующие последовательности уменьшаются в длине
#       (до полного исчезновения, если в вычитаемом было больше таких символов)
# * поддерживать умножение на натуральное число N (количество символов в последовательностях увеличивается в N раз)
# * поддерживать итератор по всем символам последовательности

class Spiral:

    def __init__(self, s):
        self.D = {}
        for item in s:
            if item in self.D:
                self.D[item] += 1
            else:
                self.D[item] = 1

    def __add__(self, other):
        qwe = Spiral("")

        a = list(self.D.keys())
        for item in other.D.keys():
            if item not in a:
                a.append(item)

        for key in a:
            if key in self.D and key in other.D:
                qwe.D[key] = self.D[key] + other.D[key]
            elif key not in self.D:
                qwe.D[key] = other.D[key]
            else:
                qwe.D[key] = self.D[key]
        return qwe

    def __sub__(self, other):
        qwe = Spiral("")
        for key in self.D:
            if key not in other.D:
                qwe.D[key] = self.D[key]
                continue
            if self.D[key] >= other.D[key]:
                qwe.D[key] = self.D[key] - other.D[key]
            else:
                qwe.D[key] = 0
        return qwe

    def __mul__(self, other):
        qwe = Spiral("")
        for key in self.D:
            qwe.D[key] = self.D[key] * other
        return qwe

    def __str__(self):
        n_letters = n_rows = n_columns = 0
        for key in self.D:
            n_letters += self.D[key]
        for i in range(1, n_letters + 1):
            if i % 2:
                if i * (i // 2) + 1 <= n_letters < ((i + 1) // 2) * (i + 2):
                    n_rows = i
                    break
            if i % 2 == 0:
                if (i + 1) * (i // 2) == n_letters:
                    n_rows = i
                    break
        for i in range(1, n_letters + 1):
            if i % 2:
                if i * (i // 2 + 1) == n_letters:
                    n_columns = i
                    break
            if i % 2 == 0:
                if i * (i // 2) - ((i - 2) / 2) <= n_letters < (i + 1) * (i // 2 + 1):
                    n_columns = i
                    break
        matrix = []
        for i in range(n_rows):
            matrix.append([0]*n_columns)
        x = y = 0
        if ((n_rows - 2) % 4 == 0 or (n_rows + 1) % 4 == 0) and ((n_columns - 2) % 4 == 0 or (n_columns + 1) % 4 == 0):
            if n_rows == n_columns and (n_rows - 2) % 4 == 0:
                y = n_rows // 2
                x = y + 1
            elif n_rows == n_columns and (n_rows + 1) % 4 == 0:
                y = (n_rows + 1) // 2
                x = y + 1
            else:
                y = n_rows // 2
                x = y + 2
        else:
            n = n_columns
            while (n - 2) % 4 != 0:
                n += 1
            x = y = n // 2
        if n_rows == n_columns == 1:
            x = y = 1
        if n_rows == 1 and n_columns == 2:
            x, y = 1, 2
        x, y = x - 1, y - 1
        res_string = ""
        for key in self.D:
            res_string += str(key) * self.D[key]
        matrix[x][y] = res_string[0]
        res_string = res_string[1:]
        reps = 1

        while 1:
            for i in range(reps):
                if not res_string:
                    break
                y += 1
                if x >= 0 and y >= 0:
                    matrix[x][y] = res_string[0]
                res_string = res_string[1:]
            if not res_string:
                break
            reps += 1

            for i in range(reps):
                if not res_string:
                    break
                x -= 1
                if x >= 0 and y >= 0:
                    matrix[x][y] = res_string[0]
                res_string = res_string[1:]
            if not res_string:
                break
            reps += 1

            for i in range(reps):
                if not res_string:
                    break
                y -= 1
                if x >= 0 and y >= 0:
                    matrix[x][y] = res_string[0]
                res_string = res_string[1:]
            if not res_string:
                break
            reps += 1

            for i in range(reps):
                if not res_string:
                    break
                x += 1
                if x >= 0 and y >= 0:
                    matrix[x][y] = res_string[0]
                res_string = res_string[1:]
            if not res_string:
                break
            reps += 1
        # print(matrix)
        for row in matrix:
            for char in row:
                if char == 0:
                    res_string += " "
                else:
                    res_string += char
            res_string += '\n'
        return res_string[:-1]

    def __iter__(self):
        for key in self.D:
            for item in list(self.D[key] * key):
                yield item
