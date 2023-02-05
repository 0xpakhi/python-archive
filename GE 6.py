#swap the first n characters of two strings

string1=input("enter the first string: ")
string2=input("enter the second string: ")
n=int(input("enter the number of digits you want to swap: "))
def swap(string1, string2, n):
    string1_new = string2[:n] + string1[n:]
    string2_new = string1[:n] + string2[n:]

    var = "new string 1 : {} & string 2 : {}".format(string1_new,string2_new)

    return var
print (swap(string1,string2,n))
