# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

list4=[1,2,3]
list5=list4[1:3]
print(list5)

list5 = myList[:3]
list6=myList[1:]
list7=myList[2:len(myList)]
list8=myList[1:-1]

print(list5)
print(list6)
print(list7)
print(list8)

del list5[:1]
del list6[:]
del list7

print(list5)
print(list6)
print(list7)
