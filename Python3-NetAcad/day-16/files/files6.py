# Writing byte array in a binary file

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

try:
    st = open('first.bin','wb')
    print('Returned by write():',st.write(data))
    st.close()
except IOError as e:
    print('Error:',strerr(e.errno))
