# Inheritance

class Star:
    def __init__(self,name,galaxy):
        self.name = name
        self.galaxy = galaxy
    # comment the __str__() method and try to print the output.
    # this method is called by python without manual invocation when it wants the object/class to return a string.
    # here we have just overridden the method to work for us.
    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun = Star('Sun','Milky Way')
print(sun)
# the hex presented by this output is Python's Internal Object Identifier.
print(sun.__dict__)
for k,v in sun.__dict__.items():
    print(k,'->',v)
