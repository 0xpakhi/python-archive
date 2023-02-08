# take as input the coefficients of a quadratic equation and determine its roots.

import math
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))

d=(b**2)-(4*a*c)

root1=(-b-math.sqrt(d))/(2*a)
root2=(-b+math.sqrt(d))/(2*a)

print ("the roots are: " ,root1, root2)
