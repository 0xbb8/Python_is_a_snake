a = 15
b = 22
log = a and b
print (log)
print (not a)
print (not b)
print (~a)
print (~b)

# OS developer example
print ("Manipulating single bit (Bit Status Check)")
flagRegister = 0x1234
print (flagRegister)
#theMask = 8
theMask = 0x8
print (flagRegister & theMask)
# the 'theMask' variable is called the "Bit Mask".
# It's used to check the bit status and also change the bit value.

# now we reset the value of the flagRegister's 3rd bit (to 0) by using another bit mask.
# the bit mask that we are going to use to change the value of our bit is the 
# negation of the 'theMask' variable.
print ("Manipulating single bit (Reset Bit)")
print(flagRegister & ~theMask)

print ("Manipulating single bit (Set Bit)")
print(flagRegister | theMask)

print ("Manipulating single bit (Negate Bit)")
print(flagRegister ^ theMask)

## Binary Left Shift and Binary Right Shift
shift = 17
rightShift = shift >> 1
leftShift = shift << 2
print ("Value:", shift)
print ("Right shift 1 bit:",rightShift)
print ("Left shift 2 bits:",leftShift)
