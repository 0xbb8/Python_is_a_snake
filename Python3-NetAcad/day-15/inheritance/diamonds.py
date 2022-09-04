# OOP: diamond inheritance.

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A,C):
    pass

obj = D()

# NOTE: The following error will occur:
# Traceback (most recent call last):
#     File "diamonds.py", line 9, in <module>
#         class D(A,C):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, C

# NOTE: MRO: Method Resolution Order
# this is the algorithm used by python to look up inheritance tree to find necessary methods.
