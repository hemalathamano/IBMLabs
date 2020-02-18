a=int(input("enter a first number "))
b=int(input("enter a second number "))
c=int(input("enter a third number "))


if(a>=b)and(a>=c):
    largest=a

elif(b>=a)and(b>=c):
    largest = b
else:
    largest = c

print("LARGEST NUMBER: ",largest)