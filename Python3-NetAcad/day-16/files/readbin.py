# Reading a bin file
# Requires a special method 'readinto()'

from os import strerror

data = bytearray(14)

try:
    st = open('first.bin','rb')
    # reading content into the bytearray named data.
    st.readinto(data)
    for i in data:
        print(hex(i),end=' ')
    st.close()
except IOError as e:
    print('Error:',strerr(e.errno))
finally:
    print()
