# import module under different names
import math as lulu

#print(math.pi) # this gives NameError
print("lulu.pi:",lulu.pi)

# also selective import works with alias also
from math import pi as pp,sin as susu
print("pp:",pp)
print("susu(pp/2):", susu(pp/2))
