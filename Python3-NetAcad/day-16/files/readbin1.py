# reading binary files using the read() method.
from os import strerror
try:
    stream = open('first.bin','rb')
    # reading the whole file in the byte array
    data = bytearray(stream.read())
    for d in data:
        print(hex(d),end=' ')
    stream.close()
except IOError as e:
    print('Error:',strerr(e.errno))
finally:
    print()

# NOTE: Best not to use this method if unsure of file contents fitting the available memory.
# if the read() method is used with an arguement: specifies the number if bytes to read
