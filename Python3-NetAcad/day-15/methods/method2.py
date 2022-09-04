# property name mangling in methods

class classy:
    # normal method
    def visible(self):
        print("visible method")
    # this is a hidden method.
    # the method is partially hidden because of the prefix '__'
    def __hidden(self):
        print("hidden method")

obj1 = classy()

obj1.visible()

try:
    # this won't work coz the method is hidden
    obj1.hidden()
except:
    print("can't do it")
# this works because of property name mangling
obj1._classy__hidden()
