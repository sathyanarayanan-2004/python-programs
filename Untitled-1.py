print("hello world")
#sum of two number
a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
c=a+b;
print(c)
#swapping two number without duplicate
x=int(input("Enter the value of X:"));
y=int(input("Enter the value of Y:"));
print("Before swaping:")
print("x=",x)
print("y=",y)
x=x+y;
y=x-y;
x=x-y;
print("After swaping:")
print("x=",x)
print("y=",y)
#check the value is positive or negative
d=int(input("Enter the value:"))
if(d==0):
    print("The Value is zero")
elif(d>0):
    print("The value is positive")
else:
    print("The Value is negative")
#change the kilometer into miles
m=int(input("Enter the kilometer:"))
n=m*0.62137;
print("The miles of m:",n)
#given year is leap year or not
f=int(input("Enter the year:"))
if(f%4==0):
    print("This is a leap year")
else:
    print("This is not a leap year")
#prime number in between the range
l = int(input ("Enter the Lowest Range Value: "))  
u = int(input ("Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (l, u + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
#fibonacci series
n = int(input("How many terms? "))
n1=0
n2=1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
# verify it is armstrong or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#sum of all integer
h=int(input("Enter the value:"))
sum=0;
i=1;
while (i<=h):
    sum =sum+h;
    i=i+1;
print("The sum is",sum)



