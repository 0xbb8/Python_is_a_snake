# see the diffrences between class and instance variables

class varias:
    # here we have a class variable.
    value = 0
    def __init__(self,val):
        # try these assignments as well
        #value = val # method's local variable
        #self.value = val # instance variable
        varias.value = val
# here we print the __dict__ of the class
# prints the value of the 'varias.value' attribute
print(varias.__dict__)
# an instance of the class
vara = varias(7)

print(varias.__dict__)
print(vara.__dict__)
