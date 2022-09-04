lst=[12,34,5,3,6,8,33,56]
largest=lst[0]
# assuming the largest any one of the list value
for i in lst:
    if i > largest:
        largest = i
print(largest)
