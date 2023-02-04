#Write a function that returns True if the year passed as parameter is a leap year and False otherwise.


def leapyear():
    year=int(input("enter the year: "))
    if year%100==0:
        if year%400==0:
            leapyear= True
        else:
            leapyear = False
    elif year%4==0:
        leapyear= True
    else:
        leapyear = False
    return leapyear

x=leapyear()
print (x)
        
