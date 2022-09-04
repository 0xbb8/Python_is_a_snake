#!/bin/python3

f="fizz"
b="buzz"
r=""
i=0
def fizzbuzz():
    global r,i
    i+=1
    if (i%3==0):
        r+=f
        if (i%5==0):
            r+=b
    elif (i%5==0):
        r+=b
    else:
        r="---"
    print(str(i)+": "+str(r))
    return fizzbuzz()
fizzbuzz()
