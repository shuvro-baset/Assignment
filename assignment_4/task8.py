salary = {'Jon': 100, 'Dan':200, 'Rob':300}
sum = 0
counter = 0
for i in salary.values():
    counter = counter + 1
    sum = i + sum
avg = sum / counter

print(sum)
print(avg)
