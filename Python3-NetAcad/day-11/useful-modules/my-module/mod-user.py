# importing my own module as a general user.
from mymod import sum_me,prod_me,__counter

mylist = [a for a in range(1,6)]

print("sum:",sum_me(mylist))
print("product:",prod_me(mylist))
print("The counter variable:",__counter)
