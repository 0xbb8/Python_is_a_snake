def factorial(num):
    fac=1
    if num < 0:return None
    elif num < 2:return 1

    for i in range(num):
        fac*=(i+1)
        print ("Factorial of",i,"is:",fac)
    return fac
# Using recursive function
# Calling own function is called recursion.
# Recursive function consumes a lot of memory.
# Recursive function must contain a termination (referred as the base case)
# condition otherwise it enters in an infinite loop.
def rec_factorial(num):
    if num < 0:return None
    if num < 2:return 1
    return num*rec_factorial(num-1)
n = int(input("Enter a number:")) 
print("Factorial of",n,"is",rec_factorial(n))
