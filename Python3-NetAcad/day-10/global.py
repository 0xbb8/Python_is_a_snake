def myFunction():
    global var
    var = 4
    print("Inside function, var =",var)
var=1
myFunction()
print("Out:",var)
