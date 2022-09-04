# Using readlines()

from os import strerror

try:
    st = open('text.txt')
    whole_file = st.readlines()
    count = 0
    for line in whole_file:
        print(line,end='')
        count += 1
    print('\nTotal lines:',count)
except IOError as e:
    print('Error:',strerr(e.errno))
