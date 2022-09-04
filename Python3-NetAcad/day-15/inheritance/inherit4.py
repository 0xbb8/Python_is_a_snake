# OOP: Multiple Inheritance
# When a subclass has more than one superclass

class Dad:
    varia = 11
    def __init__(self):
        self.var = 12
class Mom:
    varia = 21
    def __init__(self):
        self.var = 22
# This sub class has two superclass.
class Child(Mom,Dad):
    #def __init__(self):
     #   Dad.__init__(self)
      #  Mom.__init__(self)
    pass

obj = Child()
print(obj.varia, obj.var)
# NOTE: Here the superclass which is the first while defining the subclass will be given priority.
# i.e. Child(Dad,Mom) : Dad Superclass will be given priority.

# Also in multi-level inheritance, the super class just above the subclass will be given priotity.
