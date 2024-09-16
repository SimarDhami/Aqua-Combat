import random

comp =random.choice([-1,0,1])
youstr=input("enter your choice: ")
youDict={"s":1, "w":-1, "g":0}
revdict={1:"snake", 0:"gun", -1:"water"}
you=youDict[youstr]

print(f"you chose {revdict[you]}\ncomp choose {revdict[comp]}")

if(comp==you):
    print("draw")

else:
    if((comp-you)==-1 or (comp-you)==2):
        print("lose")
    else:
        print("win")

# yeh logic aaya from below
#     if(comp==-1 and you==1):-2, comp-you=-1-1=-2
#         print("win")
#     elif(comp==-1 and you==0):-1
#         print("lose")
#     elif(comp==0 and you==1):-1
#         print("lose")
#     elif(comp==0 and you==-1):1
#         print("win")
#     elif(comp==1 and you==0):1
#         print("win")
#     elif(comp==1 and you==-1):2
#         print("lose")
#     else:
#         print("something is wrong")