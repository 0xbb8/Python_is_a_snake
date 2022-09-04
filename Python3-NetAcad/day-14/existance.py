# AttributeError is caused by non-existing attributes.
# Gotta find'em

class errors:
    # this class variable is for testing hasattr()
    attr = 1
    def __init__(self,val):
        if val % 2 != 0:
            self.a = val
        else:
            self.b = val

obj1 = errors(1)
# self.a will be created by this instance.
print(obj1.a)
# The below will give an AttributeError as it's non-existant.
#print(obj1.b)

## handling using try-except
try:
    print(obj1.b)
except AttributeError:
    print('Exception Raised')

# hasattr() - function to check the existance of class/object's attributes.

print(hasattr(errors,'attr'))
print(hasattr(obj1,'attr'))
print(hasattr(obj1,'a'))
print(hasattr(obj1,'b'))
print(hasattr(errors,'a'))
