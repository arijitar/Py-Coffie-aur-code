# TRY WITH ELSE CLAUSE
# something we want to run a piece of code when try was succesful


try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
     print("Thank you")