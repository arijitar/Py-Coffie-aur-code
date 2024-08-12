# 2. write a pyhton program using function to convert celsius to fahrenheit
def celToFah(C):
   return C*(9/5)+32

cel = int(input("Enter the temparature: "))
print("Temperature in fahrenheit: ",celToFah(cel))
print(f"{celToFah(cel)}°C")

