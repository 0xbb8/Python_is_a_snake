# uses of lambda function

def myFunc(lists,func):
    for i in lists:
        print('f(', i,')=', func(i), sep='')
# This function can be replaced by a lambda function.
#def poly(x):
 #   return 2*x**2 - 4*x + 2

myFunc([x for x in range(-2,3)],lambda x : 2*x**2 - 4*x + 2)
# the function is replaces by lambda and is invoked inside the myFunc() function.

# The map() function
# Syntax:  map(function,list)

list1 = list(map(lambda x : x*2,[i for i in range(1,6)]))
print(list1)

for k in map(lambda x:x*2,[i for i in range(1,6)]):
    print(k,end=", ")
print()
