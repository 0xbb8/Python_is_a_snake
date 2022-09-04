# using while loop

from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

# Using for loop

try:
    count = 0
    stream = open('text.txt')
    # read() with no args reads the entire file
    whole_file = stream.read()
    for chars in whole_file:
        print(chars, end='')
        count += 1
    stream.close()
    print("\n\nCharacters in file:", count)
except IOError as e:
    print('Error:',strerr(e.errno))


