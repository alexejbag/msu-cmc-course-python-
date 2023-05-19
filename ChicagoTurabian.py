# Написать программу, которой на вход подаётся две строки — библиографическая ссылка B на некоторую книгу и
# внутритекстовая ссылка N на эту же книгу. программа должна проверить, что обе ссылки синтаксически верны и ссылаются
# на одну и ту же книгу. Формат ссылок — упрощённый стиль Турабьян. Вывод программы — True, если B соответствует N,
# и False — если не соответствует, или такое соответствие невозможно определить из-за синтаксической некорректности.
# Полное описание задачи — на сайте лекций.

import re
NN = N = input()
BB = B = input()
a = 0
authors = ""
result = True

N = N[N.find(' ') + 1:]
N = N[:N.rfind(' ') - 1]
B = B[:-1][::-1]
num = NN[:NN.find('.')]  # number at the beginning of N-string

publish = re.findall("\(([^)]*)\)", N)  # about publication
# ***Checking of publication***
if not publish:
    result = False
else:
    publish = publish[0]
if publish:
    pos = B.find(str(publish)[::-1])
    if pos != 0:
        result = False

title = re.findall("\.([\w\s?!)(,':-]*)\.", B)  # title of a book
# ***Checking of title***
if not title:
    title = publish
    result = False
else:
    title = title[0][::-1]
if title[0] == ' ':
    title = title[1:]

B = B[::-1]
BB = BB[:BB.rfind(title) + 1]
BB = BB[:BB.rfind('.')]
authors = BB

# ***Checking of authors***
if authors[-2] == " ":
    authors += "."
authors = authors.replace(" " + str(num), "")
authors = authors.split(",")

n = len(authors)  # 3!
if n > 1:
    authors[1] = authors[1] + " " + authors[0]
    authors = authors[1:]

if authors[0][1:] in NN and "et al." in NN:
    a = 1

if "et al." in NN and len(authors) < 4:
    result = False

if "," not in authors[0] and authors[0] in BB:
    result = False

authors = ",".join(authors)

if authors[0] == " ":
    authors = authors[1:]

if n == 3 and authors.find(", and"):
    authors = authors.replace(", and", " and")

# ***Checking of N-string***
if NN[0].isalpha() or NN[-2].isalpha():
    result = False

pos = NN.rfind(")")
if "—" in NN[pos:] or "-" in NN[pos:]:
    result = False

if num in B:
    pos = NN.find(str(num))
else:
    pos = NN.find(title)
if NN[pos-2] == '.':
    result = False


for i in [authors, title, publish]:
    if a:
        a = 0
        continue
    if i not in NN:
        result = False
        break
    if publish not in B:
        result = False
        break
print(result)
