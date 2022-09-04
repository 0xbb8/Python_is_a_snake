# Dictonary: Mutable data type, has key-value pairs
# use curly braces when declaring dictonaries
empDic={}
# can have any data type as key
keys={"hala":"Madrid", 1.2:2.3}
print(empDic)
print(keys)
print(keys[1.2])
print(len(keys))

dic={"key":"value","lock":"down","lock":"nono","val":"value"}
print(dic["key"])
# if key is the same, the key takes the later value
print(dic["lock"])
print(dic["val"])

### playing with dictionaries ###
french={"cat":"chat","horse":"cheval","dog":"chien"}
animals=["cat","dog","lion","zebra","chat"]

for animal in animals:
    ## See this searches for keys not values
    if animal in french:
        print(animal, "->", french[animal])
    else:
        print(animal,"Not in Dictionary")

# using keys() method.
# also the sorted function
print("Using keys() method and sorted() function")
for keys in sorted(french.keys()):
    print(keys,"->",french[keys])

# using the items() and values() methods
# the iten() method returns a list of tuples:->
# each tuple is a key value pair

for key,value in french.items():
    print(key,":",value)
# the value() method just returns a list of values
for values in french.values():
    print(values)
print(french.items())
print(french.values())
