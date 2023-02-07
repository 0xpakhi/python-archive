# simple calculator


a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
op = input("enter any one operator +,-,* or /: ")


if op == "+":
    print(a+b)
elif op == "-":
    print(abs(a-b))
elif op == "*":
    print(a*b)
elif op == "/":
    if b != 0:
        print(a/b)
    else:
        print("error")
else:
    print("try again")
