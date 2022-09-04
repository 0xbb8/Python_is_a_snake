# Closures : technique to store value in spite of the fact that the context in which they were created does not exist anymore.
# A closure has to be invoked in exactly the same way in which it has been declared.
def outer(par):
    loc = par
    def inner():
        return loc
    # returns a copy of the inner() function.
    return inner

var = 1
# The function returned here during the outer() invocation is a closure.
fun = outer(var)
# Here in the outer() invocation, the function is frozen along with all the enviromental elements.
# that means loc = par = 1 (the value of loc is retained), even after the function invocation is complete.
print(fun)
print(fun())

