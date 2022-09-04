# The 'yield' keyword

def fun(n):
    for i in range(n):
        return i
# NOTE: The yield keyword turns the function into a generator.
def funtus(n):
    for i in range(n):
        yield i

#for i in fun(5):
 #   print(i)
print(fun(5))
print(" - - - -")
for i in funtus(5):
    print(i)
