# Написать параметрический декоратор TypeCheck(последовательность_типов, тип_результата), который бросает исключение
# TypeError при вызове функции со следующим сообщением:
# * "Type of argument Номер is not Тип", если не совпадает тип позиционного параметра функции
#       и соответствующий ему по порядку тип в последовательности_типов
# * "Type of argument Имя is not Тип", если не совпадает тип именного параметра функции
#       и соответствующий ему тип в последовательности_типов. Типы именованных параметров перечислены в конце
#       последовательности_типов в порядке их описания в def …
# * "Type of result is not Тип", если тип возвращённого функцией значения не совпадает с типом_результата
# * "Function функция must have число arguments" — если количество переданных функции параметров
#       (включая переданные по умолчанию) не соответствует длине последовательности_типов
# Сначала проверяются параметры в порядке описания в функции, затем вызывается функция,
# после чего проеряется результат. Ислкючение возникает при первом несовпадении типа.

def TypeCheck(spisok2, tip):
    spisok = list(spisok2)
    def decorator(fun):
        def newfun(*args, **kwargs):
            # flag = [0, 0, 0]

            if len(args) + len(kwargs) != len(spisok):
                raise(TypeError("Function " + str(fun.__name__) + " must have " + str(len(spisok)) + " arguments"))

            for i, j in enumerate(args):
                if not isinstance(j, spisok[i]):
                    raise(TypeError("Type of argument " + str(i + 1) + " is not " + str(spisok[i])))

            for i, key in enumerate(kwargs):
                if not isinstance(kwargs[key], spisok[len(args) + i]):
                    raise(TypeError("Type of argument '" + str(key) + "' is not " + str(spisok[i])))

            if type(fun(*args, **kwargs)) is not tip:
                raise(TypeError("Type of result is not " + str(tip)))
            return fun(*args, **kwargs)

        return newfun
    return decorator
