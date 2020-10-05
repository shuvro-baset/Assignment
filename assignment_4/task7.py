
def Merge(marks_boys, marks_girls):
    res = {**marks_boys, **marks_girls}
    return res

marks_boys = {'Harry':15, 'Draco':8, 'Nevil':19}
marks_girls = {'Ginie':18, 'Luna': 14}
dict3 = Merge(marks_boys, marks_girls)
print(dict3)