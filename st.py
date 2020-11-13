n = (input())

v = []
c = []
dic = {"Vowel": v, "Consonant": c}

for char in n:
    if char in "aeiouAEIOU":
        if char in v:
            pass
        else:
            v.append(char)

    else:
        if char in c or char == " ":
            pass
        else:
            c.append(char)
print(dic)
