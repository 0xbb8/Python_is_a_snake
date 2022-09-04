# The 'break' and 'continue' statements.

# break - exits the loop immediately, and unconditionally ends the loop's
# operation; the program begins to execute the nearest instruction after the loop's body;

# continue - behaves as if the program has suddenly reached the end of the body;
#the next turn is started and the condition expression is tested immediately.

# break - example

print ("Use of Break")
for i in range(1,5):
    print("i = ",i)
    if i == 3:
        break
    print("Inside loop")
print("Out of it.")

print ("Use of continue")
for i in range(1,5):
    print("i = ",i)
    if i == 3:
        continue
    print("Inside loop")
print("Out of it.")
