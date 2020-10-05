a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

b = input("Enter your input: ")

a_tuple[0][2] = b
a_tuple[1][2] = b
a_tuple[2][2] = b
a_tuple[3][2] = b

print(a_tuple)