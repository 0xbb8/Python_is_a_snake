def triangle(n1,n2,n3):
    #if n1+n2<=n3:return False
    #if n2+n3<=n1:return False
    #if n1+n3<=n2:return False
    # Can be compacted as:
    return n1+n2>n3 and n2+n3>n1 and n1+n3>n2
    #return True
### Pythagorean Theorem ###
def right(n1,n2,n3):
    if not triangle(n1,n2,n3):
        return False
    if a>b and a>c:
        return a**2 == b**2 + c**2
    elif b>a and b>c:
        return b**2 == a**2 + c**2
    else:
        return c**2 == a**2 + b**2

### Heron's Formula ###
def heron(a,b,c):
    s=field=0
    if not triangle(a,b,c):
        return None
    # calculating the field of triangle
    s=(a+b+c)/2
    field=(s*(s-a)*(s-b)*(s-c))**0.5
    return field


print(triangle(1,1,3))
print(triangle(1,1,1))
print(triangle(2,2,3))

#a=float(input("Enter side 1: "))
#b=float(input("Enter side 2: "))
#c=float(input("Enter side 3: "))
"""
if right(a,b,c):
    print("Right Angled Triangle")
else:
    print("It is not.")
"""
print("Field is:",heron(1,1,4))
print("Field is:",heron(1.3,2.3,2.4))
print("Field is:",heron(1.,1.,2. ** 5.))
