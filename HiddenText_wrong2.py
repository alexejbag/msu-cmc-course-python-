b = 1
i = ""
s1 = input()
s2 = input()
len2 = len(s2)
place = s1.find(s2[0])
if len2 == 1 and place != -1:
    b = 1
elif len2 == 1 and place == -1:
    b = 0
else:
    while place != -1:
        b = 1
        ind1 = s1.find(s2[1], place + 1)
        dif = ind1 - place
        for i in s2[2:]:
            ind2 = s1.find(i, ind1 + 1)
            if (ind2 - ind1) != dif:
                b = 0
                i = "00"
                break
            ind1 = ind2
        if i == s2[len2-1]:
            break
        place = s1.find(s2[0], place + 1)
if b:
    print("YES")
else:
    print("NO")
