b = 1
s1 = input()
s2 = input()
s2_len = len(s2)
len1 = s1.find(s2[0])
if s2_len > 1:
    len2 = s1.find(s2[1], len1+1)
    dif = len2 - len1
    for i in s2[2:]:
        len1 = s1.find(i, len2+1)
        if (len1 - len2) != dif:
            b = 0
            break
        len2 = len1
if b:
    print("YES")
else:
    print("NO")
