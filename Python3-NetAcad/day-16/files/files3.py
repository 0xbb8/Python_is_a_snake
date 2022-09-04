# Counting lines and chars at once

from os import strerror

try:
    stream = open('text.txt')
    count_lines = 0
    count_chars = 0
    lines = stream.readlines()

    for line in lines:
        print(line,end='')
        count_lines += 1
        for ch in line:
            count_chars += 1
    stream.close()
    print('\nTotal Lines:',count_lines,'\nTotal Characters:',count_chars)
except IOError as e:
    print('IO Error:',strerr(e.errno))

# NOTE: for line in open('text.txt'):
# The above code returns an object which is an instance of the iterable class.
# The iteration protocol defined for the file object is very simple - its __next__ method just returns the next line read in from the file.
# NOTE: Also the object automatically invokes close() when any of the file reads reaches the end of the file.
