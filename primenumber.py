a=int(input("enter a number "))
if a>1:

  for i in range(2,a//2):

    if(a%i)==0:
        print("notprime")
        break
  else:
        print("prime")

else:
        print("not prime")


