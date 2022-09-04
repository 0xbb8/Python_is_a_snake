# trying to copy an image
# /home/k2030gautam/Python3-NetAcad/day-16/files

from os import strerror

image_name = input('Enter image name(in home dir):')
image_path = '/home/k2030gautam/' + image_name

try:
    st = open(image_path,'rb')
    data = bytearray(st.read())
    st.close()
    out = open('copied.png','wb')
    out.write(data)
    out.close()
except IOError as e:
    print('Error:',strerr(e.errno))
else:
    print('Done')
