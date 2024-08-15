# Store the multiplication table generated in problem 3 in a file name Tables.txt

n =int(input("Enter your number: "))


table =[n*i for i in range(1, 11) ]

with open("Tables.txt", "a") as f:
    f.write(str(table) + "\n")