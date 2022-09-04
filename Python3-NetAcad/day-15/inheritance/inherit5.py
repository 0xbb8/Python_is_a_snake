# OOP: Heirarchy of Classes

class One:
    def doit(self):
        print('from one')
    def doanything(self):
        self.doit()
# the method doit() is same in both classes.
class Two(One):
    def doit(self):
        print('from two')

# making two instances of both the classes.
one = One()
two = Two()
# Here we call the same method but from different objects of different classes.
one.doanything()
two.doanything()
# NOTE: Here the subclass is able to modify the superclass behaviour, this is called 'Polymorphism'. 
# The method, redefined in any of the superclasses, thus changing the behavior of the superclass, is called 'virtual'.
