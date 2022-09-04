# the 'platform' module
from platform import platform,machine,processor,system,version

# using the platform() function
print(platform(aliased=True,terse=True))
print(platform(4))
print(platform(0,7))

# using machine() function
print(machine())
# using processor() function
print(processor())
print("processor() returns blank because it could not find a generic name of this processor")
# using system() function
print(system())
# using version() function
print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())
# prints type of python implementation (cannonical or non-cannonical python branch)

for attr in python_version_tuple():
    print(attr)
# prints the major part of python version - 3, minor part of python version - 5 and patch level number - 3.
# i.e Python 3.5.3
