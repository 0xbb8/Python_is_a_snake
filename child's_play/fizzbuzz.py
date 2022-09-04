#!/bin/python3
f = "Fizz"
b = "Buzz"
r = ""
for i in range(1,101):
    if (i%3 == 0):
        r+=f
        if (i%5 == 0):
            r+=b
    elif (i%5 == 0):
        r+=b
    else:
        r="---"
    print(str(i) + ": " + str(r))
    r=""
