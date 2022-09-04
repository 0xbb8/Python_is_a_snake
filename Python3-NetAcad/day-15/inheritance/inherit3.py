# OOP: INheritance

class Super:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'My name is ' + self.name

class Sub(Super):
    def __init__(self,name):
        # NOTE: You can invoke the superclass's method from the sub class.
        Super.__init__(self,name)

sub = Sub("Sandesh")
print(sub)
# NOTE: Given the output and the fact that there is no __str__() method in the Sub class.
# The conclusion is that the __str__() method was inherited by the Sub class from Super class.
print()
print('*******************************************************')
print()

class Parent:
    def __init__(self,name):
        self.name = name
        self.inst_var = 9876

    def __str__(self):
        return 'My lastname is ' + self.name

# checking if this works
class mid(Parent):
    cls_var = 1234567

class Child(mid):
    def __init__(self,name):
        # NOTE: here the super() function creates the context where you don't have to pass the 'self' arguement
        # to access the superclass' properties.(here we access the constructor but any property can be accessed)
        super().__init__(name)

child = Child('Gautam')
print(child)
print("Accessing Class Variable:",child.cls_var)
print("Accessing Instance Variable:",child.inst_var)
