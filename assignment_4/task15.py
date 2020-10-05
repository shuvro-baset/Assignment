
list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]


answer = {}
for key, value in list:
  if key in answer:
    answer[key].append(value)
  else:
    answer[key] = [value]

print(answer)