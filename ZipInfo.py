# Условие: https://uneex.org/LecturesCMC/PythonIntro2020/Homework_ZipInfo

import re
import io
import sys
from zipfile import ZipFile

txt1 = sys.stdin.read()
txt = bytes.fromhex(txt1)

with io.BytesIO(txt) as F:
    F = ZipFile(F)
    lst = F.infolist()

count_files = 0
sum_size = 0
for i in lst:
    # print(">>>", i)
    plus = re.findall("file_size=(\d+)", str(i))
    if plus:
        sum_size += int(plus[0])
        count_files += 1

print(count_files, sum_size)
