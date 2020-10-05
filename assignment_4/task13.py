
dict = {'A': [1,2,3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
total = 0

for value in dict:
    value_list = dict[value]
    count = len(value_list)
    total += count

print(total)