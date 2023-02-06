#Write function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys


def cubenum():
    a=[1,2,3,4,5,]
    b=[1,8,27,64,125]
    c=zip(a,b)
    d=dict(c)
    return d

y=cubenum()
print (y)



