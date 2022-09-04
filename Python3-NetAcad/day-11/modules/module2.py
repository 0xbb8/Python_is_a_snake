# from <module name> import <only these entities>
from math import e,pi,sin
# from math import 8
# Imports all the entities from the math module
# this type of import method will not require qualification of the entities for them to be useable
print(e)
print(pi)
print(sin(1/2 * pi))
# should not use qualification. NameError will be thrown.
#print(math.e)
