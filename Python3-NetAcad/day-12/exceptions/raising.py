# Manually raising an TypeError exception
def whyraise():
    print("Before")
    raise TypeError
    print("After")
#whyraise()
#print("After invocation")
# handling my own exception/
try:
    whyraise()
    print("After Invocation")
except TypeError:
    print("I awakened the demon. I put it down.")

### Only using the 'raise' keyword : re-raise the same exception ##

def rere():
    try:
        return 1/0
    except ArithmeticError:
        print("Raised once.")
        raise
try:
    rere()
except ArithmeticError:
    print("Raised twice")
print("Now i am free")
