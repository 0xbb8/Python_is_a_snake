# Comparing string with the operators ==,!=,<,>,<=,>=
# These operators will compare the strings code point by code point

print('alpha' == 'Alpha')
print('alpha' != 'beta')
print('20' > '020')
print('30' <= '90')
print('asdasd' > 'AKJHKHDKH')

print('10' == '101')
print('10' == 10)
print('20' != 20)

# Sorting a list of strings.

melist = ['This', 'is', 'a', 'list', 'of', '123', '-', 'numbers,', '@#$', '-', 'characters', 'and', 'abc', '-', 'alphabets.']
print('Original list:\n',melist)

# sorted() function - does not affect the original list
sortedList = sorted(melist)
print('Sorted list is (using sorted() function):\n',sortedList)

# sort() method - performs the sorting in situ - changes are made to the original list
melist.sort()
print('Sorting using method sort():\n',melist)
