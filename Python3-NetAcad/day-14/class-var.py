# this is an example of a class variable.

class class_vars:
    # here we initialize the variable 'counter'.
    # it is inside the class code but outside any of the class methods.
    # these types of variables are called 'Class Variables'
    #counter = 0
    print("hey,OH")
    __counter = 0
    def __init__(self,val=1):
        self.__first = val
        class_vars.__counter += 1

obj1 = class_vars()
print(obj1.__dict__,obj1._class_vars__counter)
obj2 = class_vars(2)
print(obj2.__dict__,obj2._class_vars__counter)
obj3 = class_vars(3)
print(obj3.__dict__,obj3._class_vars__counter)
print("After all creations")
print(obj1.__dict__,obj1._class_vars__counter)
print(obj2.__dict__,obj2._class_vars__counter)
print(obj3.__dict__,obj3._class_vars__counter)
