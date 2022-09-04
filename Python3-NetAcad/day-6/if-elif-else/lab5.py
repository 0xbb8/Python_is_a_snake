income = float(input("Enter the annual income: "))

limit = 85528

if income <= 85528:
    tax = (0.18*income) - 556.2
elif income > 85528:
    tax = 14839.2 + 0.32*(income - 85528)
if tax < 0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
