# Write a recursive function to calculate the sum of first n natural numbers

def findsum(n):
   sum = 0
   i = 1
   # for i in range (1,n+1):
   while i <= n:
      sum+=i
      i = i+1
   return sum
print(findsum(10))