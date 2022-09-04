# The negation of a conjunction is the disjunction of the negations.
var = 1
print (not(var < 0 and var > 0))
print (not(var < 0) or not(var > 0))

# The negation of a disjunction is the conjunction of the negations.
print (not(var < 0 or var > 0))
print (not(var < 0) and not(var > 0))
