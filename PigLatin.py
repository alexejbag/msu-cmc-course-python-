# Согласно правилам «поросячьей латыни» английские слова при разговоре преобразуются так:
# * если слово начинается на согласную — эта согласная переносится в конец слова, после чего добавляется «ay»: "latin" ⇒ "atinlay"
# * если слово начинается на несколько согласных, они все переносятся в конец слова, после чего добавляется «ay»: "stupid" ⇒ "upidstay"
# * если слово начинается на гласную, "aouie" (не "y"!) и имеет более одного слога, лидирующая гласная и все согласные за ней переносятся в конец с добавлением «ay»: "under" ⇒ "erunday" (в Википедии это второй вариант)
# * для нашего удобства непроизносимые гласные тоже считаются слогом, например "are" ⇒ "earay"; (так исторически не было: язык всё-таки разговорный)
# * односложные слова, начинающиеся на гласную, просто дополняются «yay»: "egg" ⇒ "eggyay"
# * апостроф считается согласной, а дефис — разделителем (опять-таки для простоты)
# * слова без гласных не изменяются
# Написать программу, которая построчно вводит «английский» текст (текст, содержащий последовательности латинских букв
# и другие символыi; последняя строка пустая) и выводит перевод на поросячью латынь (для простоты любая посл-ть
# английских букв с гласными считается словом). Обратите внимание на то, что слово, написанное со прописной буквы,
# в поросячьей латыни также пишется со прописной буквы. Более одной прописной буквы в слове не встречается.

import re
vowels = "aeiou"
prefix = pig_word = ""
flag = 0
s = input()
while s:
    s += ' '
    e = re.findall("([(\"\d]*)([a-zA-Z']*)([^a-zA-Z'])", s)  # ([\d\s\[-`:-@!-&(-/~{-}№])", s)
    for i, j in enumerate(e):
        e[i] = list(j)
    for j in e:
        if j[1]:
            if 'A' <= j[1][0] <= 'Z':
                flag = 1
        word = j[1] = j[1].lower()

        if '-' in word:
            pos = word.find('-')
            prefix = word[:pos + 1]
            word = word[pos + 1:]

        if len(re.findall("[aeiou]", word)) == 0:
            pig_word = word
        elif len(re.findall("[aeiou]", word)) == 1 and word[0] in vowels:
            pig_word = word + "yay"
        elif word[0] not in vowels:
            lst = list(re.findall("([aeiou])([\w']*)", word)[0])
            pos = word.find(lst[0])
            pig_word = lst[0] + lst[1] + word[:pos] + "ay"
        elif len(re.findall("[aeiou]", word)) > 1 and word[0] in vowels:
            count = 0
            pos = 0
            for k in word:
                if k in vowels:
                    count += 1
                    if count == 2:
                        break
                pos += 1
            pig_word = word[pos:] + word[:pos] + "ay"

        j[1] = prefix + pig_word
        prefix = postfix = ""
        if flag:
            j[1] = j[1].capitalize()
            flag = 0
    result = ""
    for j in e:
        result += j[0] + j[1] + j[2]
    result = result[:-1]
    print(result)
    s = input()
