# More on closures

def my_closure(par):
    loc = par
    def power(value):
        return value ** loc
    return power

square = my_closure(2)
cube = my_closure(3)

print('i Sq Cu')
for i in range(1,6):
    print(i,square(i),cube(i))
