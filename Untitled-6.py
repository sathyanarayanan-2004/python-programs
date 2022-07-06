f=int(input("Enter the year:"))
if(((f%4==0) & (f%100!=0))| (f%400==0)):
    print("This is a leap year")
else:
    print("This is not a leap year")