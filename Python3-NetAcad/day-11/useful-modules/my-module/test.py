# import ing the 'path' list from module 'sys'
from sys import path
# printing all the module path stored in the list path
# this is where python stores all the module path name .
# the path will be varied according to the OS you work on.
print ("All module paths from the list 'path of module sys' are:")
for i in path:
    print(i)
