# pyramid shaped '*' pattern for any odd number of rows
rows = int(input("enter rows: "))
i = 1
while i <= rows:
    if i == 1:
        print(' '*(rows-i)+"*")
    else:
        print(' '*(rows-i) + "*"*(i-1))
    i += 1
