# the 'is' operator in python.

class isop:
    def __init__(self,val):
        self.val = val

ob1 = isop(0)
ob2 = isop(2)
# here ob1 and ob3 are the variables refering to the same object.
ob3 = ob1
# NOTE: Variables don't store the values themselves but handles pointing to the internal python memory.
ob3.val += 1
# the 'is' operator checks whether the variables refer to the same object.
print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val,ob2.val,ob3.val)

str1 = 'Mary died in '
str2 = 'Mary died in Yemen'
str1 += 'Yemen'
# the the '==' just compares the value, the 'is' operator checks the object itself.
print(str1 == str2, str1 is str2)
