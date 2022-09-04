# get properties from superclass to a newly created subclass.
# you get all the properties from the superclass but can also add new properties
# you can even override the superclass' properties.

# superclass of all
class Dad:
    pass
# subclass of Dad
class Son(Dad):
    pass
# subclass of both Dad and Son
class Grandson(Son):
    pass

# let's ask python about the relation of the classes.
classes = [Dad,Son,Grandson]
classess = ['Dad', 'Son', 'Grandson']
print('Classes:',classess)
print('issubclass()')
for class1 in classes:
    print(class1.__name__,'->\t',end='')
    for class2 in classes:
        # NEW ESCAPE CHAR: '\t' for a <tab> 
        print(issubclass(class1,class2),end='\t')
    print()

# isinstance() function checks if the whether it's and object of the class or not
print('isinstance()')
dad = Dad()
son = Son()
grandson = Grandson()
i=0
for obj in [dad,son,grandson]:
    print(classess[i].lower(),'->\t',end='')
    i+=1
    for class3 in classes:
        print(isinstance(obj,class3),end='\t')
    print()

