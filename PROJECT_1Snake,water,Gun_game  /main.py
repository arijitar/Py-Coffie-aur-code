import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = int(input("Enter your choice: "))
youDict = {"S": 1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"Water", 0:"g"}

you = youDict[youstr]

print(f"You chose {youDict[you]}\ncomputer choice {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You lose!")
    elif(computer == 0  and you == 1):
        print("You lose!")
    else:
        print("Something went wrong!")
if((computer - you) == 1 or (computer - you) == 2 ):
    print("you Lost")
else:
    print(" you win")
    