def checker(line):
    try:
        if 'ПРОЦ' == line[:4]:
            return True
    except:
        pass
    return False

def func(line, depth = 0):
    if depth == 4:
        if checker(line.decode('koi8-r')):
            print(line.decode('koi8-r'))
            return True
        return False
    for code1 in codes:
        for code2 in codes:
            if code1 != code2:
                try:
                    newline = line.decode(code1).encode(code2)
                    if checker(newline.decode('koi8-r')):
                        print(newline.decode('koi8-r'))
                        return True
                    res = func(newline, depth + 1)
                    if res:
                        return True
                except:
                    pass

codes = ["utf8", "koi8-r", "CP1251", "CP866"]
line = "d0aed091e2959ed19120d0a6d094"
line = bytes.fromhex(line)
# codes = input().split()
# line = bytes.fromhex(input())
func(line)
