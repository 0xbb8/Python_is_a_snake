# importing random, seed function from random  module
from random import random,seed
# setting seed as with a fixed value.
seed(0)
print("WIth a fixed seed value")
# because of fixed seed, the random values on each instance will be near identical.
for i in range(5):
    print(random())
print()
print("Now with current time as seed()")
# now with setting the current time as the seed value
seed()
for i in range(5):
    print(random())

# NOW for random value ranges.
from random import randrange,randint

print(randrange(1),end=' ')
print(randrange(0,1),end=' ')
print(randrange(0,1,1),end=' ')
print(randint(0,1),end=' ')
print()

# randoms within 1 and 10: 1 <= x < 10

for i in range(10):
    print(randint(1,10),end=", ")
print()
# using choice() and sample()
# choice(lst) - choses a random value from a sequence 'lst' (here:list).
# sample(lst,x) - builds a list out of input sequence of 'x' elements.
from random import choice,sample
lst=[]
for i in range(10):
        lst.append(randint(1, 10))
        print(lst)
        print(choice(lst))
        print(sample(lst,5))
        print(sample(lst,10))

