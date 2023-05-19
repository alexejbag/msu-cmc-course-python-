# Условие: https://uneex.org/LecturesCMC/PythonIntro2020/Homework_TotalBnopnya

def fun(txt, depth):
    if depth > 4:
        return 0
    try:
        if txt.decode('koi8-r').find("ПРОЦ") == 0:
            print(txt.decode('koi8-r'))
            return 1
    except:
        pass

    for i in lst:
        # print(">>>i:", i)
        for j in lst:
            if i == j:
                continue
            # print("  >>>j:", j)
            try:
                newtxt = txt.decode(i).encode(j)
                if newtxt.decode('koi8-r').find("ПРОЦ") == 0:
                    print(newtxt.decode('koi8-r'))
                    return 1
                if fun(newtxt, depth + 1):
                    return 1
            except:
                pass


s1 = input()
lst = s1.split(' ')
s2 = input()
txt = bytes.fromhex(s2)
fun(txt, 1)

# utf8 koi8-r CP1251 CP866 ISO8859-1 ISO8859-5 mac-arabic cp1140