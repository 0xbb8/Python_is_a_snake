numbers=[1,2,345,67,-12,12.11,-14.3,"This is string"]
# print all the elements
print(numbers)
# print specific elements in the list.
# lists are indexed from 0..n
print(numbers[0])
print(numbers[5])
# changing the value of a certain element.
numbers[1] = "changed"
print(numbers)
# also assigning from within
numbers[3]=numbers[2]
print(numbers)
# length of the list
print("List length, len() function:",len(numbers))
st="This is sandesh"
#i=1243, len() does not work on numbers
print("len() works on string also:",len(numbers))
# removing an element using instruction 'del'.
print("(List after deleting) numbers =",end=" ")
del numbers[7]
print(numbers)
# Negative indices are legal in python.
print("Negative indices:","Where -1 refers to the last one in the list","-2 refers to second to last element and so on.",sep="\n",end="Examples are -7 and -1\n")
print(numbers[-7])
print(numbers[-1])
print()
print("Nested list")
list1 = [1,2,3,["red","green","blue"],4,5,6]
print(list1)

# del list1 -> deletes the whole list
