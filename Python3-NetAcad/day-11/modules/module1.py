# import a module(math) using instruction 'import'
import math

def sin():
    print("The sin() function already exists in the math module.\n \
            But DOESNOT enter my code's namespace.")
    # making pi as a vcariable in our namespace
    global pi
    pi = 3.14
sin()
print("pi from mu code:",pi)

# to use the module's entities you have to qualify the entities with the module name.
print("sin(1/2) from math module:",math.sin(1/2))
print("Pi from math module:",math.pi)
