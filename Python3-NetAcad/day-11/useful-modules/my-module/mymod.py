# this is my module. i made it myself.

## this module has two functions. sum_me() and prod_me()
# they take list as an arguement and return sum and product resp.
## Also we have a counter variable following the convention.(_counter or __counter)

__counter = 0

def sum_me(lst):
    global __counter
    __counter += 1
    sum = 0
    for i in lst:
        sum+=i
    return sum

def prod_me(lst):
    global __counter
    __counter += 1
    prod = 1
    for i in lst:
        prod*=i
    return prod

### Now we run some tests using the __name__ variable
if __name__ == "__main__":
    print("Cast me as a module.",__name__)
    l=[a+1 for a in range(5)]
    print(sum_me(l)==15)
    print(prod_me(l)==120)
else:
    print("You imported the module",__name__)
