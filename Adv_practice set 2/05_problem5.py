# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
 
l= [12*i for i in range(1, 11)]

def max(a,b):
    if(a>b):
        return a
    return b

f = reduce(max, l)

print(f)