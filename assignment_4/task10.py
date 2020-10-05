book_shop = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
max=0
new_shop={}
for key,value in book_shop.items():
    if value>max:
        max=value
        max_value=key
print("The highest selling book genre is: ", max_value, "and the number of books sold are",max)