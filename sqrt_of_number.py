#ax^2+bx+c=0

import cmath
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))

d=(b**2)-(4*a*c)

root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)

print ("the roots are: " ,root1, root2)
