# the filter() function

list1 = [x for x in range(1,6)]
# using filter() : takes arguments like the map() function
list2 = list(filter(lambda x: x>2,list1))
# NOTE: The filter() filters the second arguement with the guidance from the function in the first arguement
print(list1)
print(list2)
