# using bytearray

# NOTE: bytearrays are <mutable>, <subject to len() function>, <elements can be accessed through conventional indexing>

# NOTE: Bytearray elements must always be integers && bytearray value range is 0 - 255 (inclusive)

# You can treat bytearray elements like a integer file.

data = bytearray(255)
l = len(data)
c = 0

for i in range(len(data)):
    data[i] = l - i
it = [val*8 for val in range(1,33)]

for i in data:
    print(hex(i),end="  ")
    c += 1
    if c in it:
        print()
print()
