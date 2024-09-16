import random
'''
1 for snake
-1 for water
0 for gun
'''

comp =random.choice([-1,0,1])
youstr=input("enter your choice: ")
youDict={"s":1, "w":-1, "g":0}
revdict={1:"snake", 0:"gun", -1:"water"}
you=youDict[youstr]

print(f"you chose {revdict[you]}\ncomp choose {revdict[comp]}")

if(comp==you):
    print("draw")

else:    
    if(comp==-1 and you==1):
        print("win")
    elif(comp==-1 and you==0):
        print("lose")
    elif(comp==0 and you==1):
        print("lose")
    elif(comp==0 and you==-1):
        print("win")
    elif(comp==1 and you==0):
        print("win")
    elif(comp==1 and you==-1):
        print("lose")
    else:
        print("something is wrong")




# #from chatgpt
# import random

# # Define the possible options
# choices = ["snake", "water", "gun"]

# # Get the user's choice
# user_choice = input("Enter your choice (snake, water, gun): ").lower()

# # Get the computer's random choice
# computer_choice = random.choice(choices)

# # Print the choices
# print(f"\nYou chose: {user_choice}")
# print(f"Computer chose: {computer_choice}\n")

# # Determine the winner
# if user_choice == computer_choice:
#     print("It's a tie!")

# elif user_choice == "snake":
#     if computer_choice == "water":
#         print("Snake drinks water! You win!")
#     else:
#         print("Gun shoots snake! Computer wins!")

# elif user_choice == "water":
#     if computer_choice == "gun":
#         print("Water sinks gun! You win!")
#     else:
#         print("Snake drinks water! Computer wins!")

# elif user_choice == "gun":
#     if computer_choice == "snake":
#         print("Gun shoots snake! You win!")
#     else:
#         print("Water sinks gun! Computer wins!")

# else:
#     print("Invalid input! Please enter either 'snake', 'water', or 'gun'.")
