# list comprehension

row=[]
for i in range(8):
    row.append("pawn")
print(row)
# can be written as:
column=["pawn" for i in range(8)]
# this is an example of list comprehension
print(column)
# more examples
squares=[i**2 for i in range(8)]
print(squares)
# uses the list squares to prinrt odd squares
odds=[x for x in squares if x%2!=0]
print(odds)
