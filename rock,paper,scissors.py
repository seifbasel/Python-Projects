import random
a1="rock"
a2="paper"
a3="scissor"
list=[a1,a2,a3]
user_choice=int(input("chose 1 for rock / 2 for paper / 3 for scissor "))
com_choice=random.randint(1,3)
print("you chose :", list[user_choice-1])
print("computer chose :" ,list[com_choice-1])

if user_choice == 1 and com_choice == 1 or user_choice == 2 and com_choice == 2 or user_choice == 3 and com_choice == 3:
    print("it is a tie")
elif user_choice == 1 and com_choice == 3 or user_choice == 2 and com_choice == 1 or user_choice == 3 and com_choice == 2:
    print("you win ")
else:
    print("you lose ")