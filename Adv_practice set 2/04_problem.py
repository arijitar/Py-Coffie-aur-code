# Write program to filter a list of numbers which are divisible by 5

l= [12*i for i in range(1, 11)]

def division(n):
    if(n%5==0):
        return True
    return False

f = list(filter(division, l))
print(f)