# Writing to a file.
from os import strerror

try:
    # in 'wt' mode, the file is created if it doesn't exist.
    stream  = open('new1.txt','wt')
    for i in range(10):
        string = 'line #' + str(i) + '\n'
        # passing the string as an arguement will record the characters in the file.
        stream.write(string)
    # don't forget to close the stream. It is good practice.
    stream.close()
except IOError as e:
    print('Error:',strerr(e.errno))
