# 1. Write a program using functions to find greatest of three numbers

def greatest(a,b,c):
    if(a>b and a>c):
       print("a is greatest")
    elif(b>a and b>c):
       print("b is greatest")
    elif(c>a and c>b):
       print("c is greatest")


x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
z = int(input("Enter the number: "))

greatest(x,y,z)










