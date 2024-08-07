# 1. Write a program using functions to find greatest of three numbers

def greatest(a,b,c):
    if(a>b and a>c):
       print("a is greatest")
    elif(b>a and b>c):
       print("b is greatest")
    elif(c>a and c>b):
       print("c is greatest")


# x = int(input("Enter the number: "))
# y = int(input("Enter the number: "))
# z = int(input("Enter the number: "))

# greatest(x,y,z)


# 2. write a pyhton program using function to convert celsius to fahrenheit
def celToFah(C):
   return C*(9/5)+32

# cel = int(input("Enter the temparature: "))
# print("Temperature in fahrenheit: ",celToFah(cel))
# print(f"{celToFah(cel)}°C")

# How do you prevent a python print() function to print a new line at the end.

# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# Write a recursive function to calculate the sum of first n natural numbers

def findsum(n):
   sum = 0
   i = 1
   # for i in range (1,n+1):
   while i <= n:
      sum+=i
      i = i+1
   return sum
# print(findsum(10))

'''Write a program using function to print first n lines of the following pattern
***
**             -for n = 3
*
'''

def pattern (n):
   if(n==0):
      return
   print("*" *n)
   pattern(n-1)

pattern(3)

# Write a python function to convert inch to cm

def inch_to_cm(inch):
   return inch*2.54

n=int(input("Enter value in inches: "))
print(f"Teh corresponding value in cms is {inch_to_cm(n)}")