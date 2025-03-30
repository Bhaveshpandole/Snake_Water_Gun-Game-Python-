'''
1 for snake
-1 for water
0 for gun
'''
#random is a built in module

import random                                               

computer = random.choice([1,-1,0])

you = input("Enter your choice here: ")

youDict = {"s": 1, "w": -1, "g": 0}

younum = youDict[you]

print(f"Computer choose : {computer}")

if(computer == younum):
    print("Its Draw the match!")

elif(computer == 1 and younum == -1):
    print("You lose!")

elif(computer == 1 and younum == 0):
    print("You Win!")

elif(computer == -1 and younum == 1):
    print("You Win!")

elif(computer == -1 and younum == 0):
    print("You lose!")

elif(computer == 0 and younum == 1):
    print("You Lose!")

elif(computer == 0 and younum == -1):
    print("You Win!")

else:
    print("Something went wrong")
