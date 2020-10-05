bank = {'customer1':101, 'customer2':102, 'customer3':101, 'customer4':103, 'customer5':102}

temp = []
res = dict()
for key, val in bank.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)