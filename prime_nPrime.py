n = int(input())

p = []
np = []
c = 0
dic = {"prime": p, "non-prime": np}
for z in range(n):
    number = int(input())
    if number == 1:
        # p.append(number)
        # p[z] = p[number]
        dic["prime"] = p[number]

    else:
        for i in range(2, number):
            if (number % i) == 0:
                np.append(number)
                # dic["non-prime"] = np[number]
                break
        else:

            p.append(number)

# dic = {"prime": p, "non-prime": np}
print(dic)
