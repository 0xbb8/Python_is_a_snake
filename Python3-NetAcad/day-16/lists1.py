# more on list comprehensions

lst = []
lst1 = []
for i in range(10):
    lst.append(i if i % 2 == 0 else '*')
print(lst)

lst1 = [x for x in range(10)]
print(lst1)

# using list comprehension with the conditional expression

great = [1 if val % 2 == 0 else 0 for val in range(10)]

print(great)

#NOTE: also if there is parenthesis instead of braces, it becomes a generator

gen = (1 if val % 2 == 0 else 0 for val in range(10))
print(gen)

print(gen)

print(len(great))

try:
    print(len(gen))
except Exception as e:
    print(e.__str__())
