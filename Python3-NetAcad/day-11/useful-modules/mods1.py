# import whole module math
import math
# dir(math) gives alphabetically sorted list of all the names in the math module
names= dir(math)
print(dir(math))
# names[0] works because names is the list
print(names[0])
# all the names iterated by for loop
for name in names:
    print(name)
