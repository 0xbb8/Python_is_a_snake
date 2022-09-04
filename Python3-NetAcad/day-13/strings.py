# Unicode/UTF-8 is commonly used and has I18N

# whitespaces are counted as an element in string even if you can't see them
print("len:",len("hello world"))

# string operations:
# concatination
print("Sandesh"+"Gautam")
# replicaiton
print("tres " * 3)

# or() - ordinal function : prints the ASCII value of a single character arguement

print(ord('a'))
print(ord('@'))

# chr() - character function : prints the character from the supplied code point.

print(chr(97))
print(chr(945))

# Indexing strings
name = "Sandesh"
for i in range(len(name)):
    print(name[i],end="")
print()

# Iretating strings
for i in name:
    print(i)

# slices of strings : almost similar to lists

print("[2:]",name[2:])
print("[:]:",name[:])
print("[1:2]:",name[1:2])
print("[::3]:",name[::3])
print("[-4,-1]:",name[-4:-1])

# 'in' and 'not in' operators in strings

print("'S' in name:",end=" ")
print('S' in name)
print("'d' not in name:",end=" ")
print('d' not in name)

### strings are immutable in python
## del(with index), append() and insert() are illegal against strings
# you can use del without index

del name
#print(name) # gives error

# You can use concatination stratergies instead of append() and insert()

str = "trin"
str += "g"
str = "S" + str
print(str)

# max() and min() functions can also be used for strings
print("max('String'):",max(str))
print("min('String'):",min(str))

# index() method for strings : indexes the first element in the sequence it finds

print("hello world".index('h'))
print("hello world".index('o'))

# list() and count() function in strings

# list() - changes the string sequence in to a list, elements are each chat of the string
strings = "StRinGs"
print(list(strings))
# count() - method - counts the occurence of a character in the string sequence
print(strings.count('s'))
