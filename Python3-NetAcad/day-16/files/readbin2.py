# Reading specific number of bytes.

#NOTE: read() method with an arguement will read specific number of bytes.
# The arguement specifies the maximum number of bytes to read.

from os import strerror

try:
    stream = open('first.bin','rb')
    data = bytearray(stream.read(5))
    stream.close()

    for d in data:
        print(hex(d),end=' ')
except IOError as e:
    print('Error:',strerr(e.errno))
finally:
    print()
