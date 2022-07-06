a=str(input("The original string is : "))
n=int(input("The position of the element you want:"))
b = ""
for i in range(len(a)):
    if i != n:
        b = b + a[i]
print ("The string after removal of i'th character : " + b)