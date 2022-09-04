# Using the 'yield' keyword.
# Making my own generator: Generates the first powers of 2

def power(n):
    pow = 1
    for w in range(n):
        yield pow
        pow *= 2

for i in power(5):
    print(i)

# Using the generator in a list comprehension
myList = [num for num in power(8)]
# Using generator with the list() function
another = list(power(10))
print(myList)
print(another)
