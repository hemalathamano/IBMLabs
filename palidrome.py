str=str(input("enter a string: "))
revstr=reversed(str)

if list(str) == list(revstr):
    print("palidrome")
else:
    print("not palidrome")