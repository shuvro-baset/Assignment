
dict1 = {'a': 10, 'b':20, 'c':30}
dict2 = {'a': 10, 'c':20, 'd':30, 'e':40}

def merge_dictionaries(dict1, dict2):
    merged_dictionary = {}

    for key in dict1:
        if key in dict2:
            new_value = dict1[key] + dict2[key]
        else:
            new_value = dict1[key]

        merged_dictionary[key] = new_value

    for key in dict2:
        if key not in merged_dictionary:
            merged_dictionary[key] = dict2[key]

    return merged_dictionary
result = merge_dictionaries(dict1, dict2)
print(result)