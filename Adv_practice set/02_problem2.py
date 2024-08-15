# Write a program to print third, fifth, and seventh element from a list using enumerate function

l = [23, 43, 19, 54, 76, 82, 100, 29]

for i, item in enumerate(l):
     if i == 2 or i == 4 or i==6:
           print(item)

