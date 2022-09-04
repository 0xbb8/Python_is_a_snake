# this will print the whole exception tree.

def PrintExceptionTree(exception_class,nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(exception_class.__name__)

    for subclass in exception_class.__subclasses__():
        PrintExceptionTree(subclass, nest + 1)

PrintExceptionTree(BaseException)
