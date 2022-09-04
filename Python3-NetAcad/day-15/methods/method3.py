# some properties

class classy:

    def __init__(self):
        pass
    def visible(self):
        pass
    def __hidden(self):
        pass

obj = classy()

print(obj.__dict__)
print(classy.__dict__)

print(type(obj))
print(type(obj).__name__)
print(classy.__name__)

print(obj.__module__)
print(classy.__module__)

print(classy.__bases__)
print(classy.__bases__)
