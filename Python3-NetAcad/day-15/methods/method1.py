# here i will write my method.

# Method without any extra parameters.
# there is always a parameter 'self' in a method.
# any additional parameters can be added after the 'self' parameter
class first:
    varia = 67
    def __init__(self):
        print("Init")
    def pupu(self):
        print("pupu")

    # Method with a parameter.
    def lulu(self,var):
        vari = var
        try:
            var = float(var)**3
        except:
            print("Unsupported value")
        print(vari,"** 3:",var)
        # the 'self' parameter can also be used to call other methods.
        self.pupu()

    def call_me(self):
        print(self.varia,self.var)


obj1 = first()
obj1.pupu()
# passing the parameter
obj1.lulu(3)
obj1.lulu(input("Enter a number: "))

# the self function can also be used to access object's instance and class variables.
obj1.var = 22
obj1.call_me()
