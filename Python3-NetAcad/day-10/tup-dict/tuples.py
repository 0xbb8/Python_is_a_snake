### Tuples : Immutable sequence types
tuple1 = 1,2,3,4
tuple2 = (1.2,3.3,45,5)
emptyTuple = ()
# to seperate it from any one element variable, we end tuple with a comma
singleElement = 3,
singleWP = (1,)

print(tuple1)
print(tuple2)
print(emptyTuple)
print(singleElement)
print(singleWP)

# working with tuples : Accessing tuples
print()
tuples = (1.2,3,4,-21,45,1293)
print("Tuples:",tuples)

print(tuples[2])
print(tuples[-1])
print(tuples[:-2])
print(tuples[1:])

for elements in tuples:
    print(elements)

# Working with tuples
myTuples = (1,20,300)

# joining tuples
join = myTuples + (4000,)
multiply = myTuples * 2

print(len(join))
print(myTuples)
print(join)
print(multiply)
print(4000 in join)
print(1 not in multiply)

# more operations on tuples
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# using the tuple() function

tuputupu = tuple((1,2,3.4,"sandesh","gautam"))
print(tuputupu)
