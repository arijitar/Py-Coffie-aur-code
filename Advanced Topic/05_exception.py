# There are many built-in exceptions which are rasied in python when something goes wrong.

# Exception in python can be handled using a try statement. The code that handles the exception is writen in the except clause.

'''
try:
    # code which might throw exception

except Exception as e:
    print(e)

'''

'''
try:
   #code
except zeroDivisionError:
   #code
except TypeError:
   #code
except:
   #code            # All other exceptions are handled here.
'''

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("heyyyy")
    print(v)

print("Thank you")