### Fibonacci Number ###
# Fib(n) = Fib(n-1) + Fib(n-2)
def fib(n):
    if n==0:return 0
    elif n<0:return None
    if n<3:return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for i in range(6):
    print(i,"->",fib(i))
fibb=[0,1,1,2,3,5,8,13,21,34,55,89,144]

# OR user recursive function: Function that calls itself
print("Using recursive funciton below")
def rec_fib(n):
    if n == 0:
        return 0
    elif n < 1:
        return None
    if n < 2:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)


for i in range(6):
    print(i,"->",rec_fib(i))
