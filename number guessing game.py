import random
from turtle import clear

logo = """
                                 _    _                                      _                 
                                | |  | |                                    | |                
   __ _  _   _   ___  ___  ___  | |_ | |__    ___   _ __   _   _  _ __ ___  | |__    ___  _ __ 
  / _` || | | | / _ \/ __|/ __| | __|| '_ \  / _ \ | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__|
  | (_| || |_| ||  __/\__ \\__ \ | |_ | | | ||  __/ | | | || |_| || | | | | || |_) ||  __/| |   
  \__, | \__,_| \___||___/|___/  \__||_| |_| \___| |_| |_| \__,_||_| |_| |_||_.__/  \___||_|   
   __/ |                                                                                       
  |___/                                                                                        

"""
numbers_list = []
for i in range(101):
    numbers_list.append(i)

def hard():
    the_number = random.choice(numbers_list)
    remaining_lives=5
    for j in range(5):
        print(f"remaining lives is {remaining_lives}")
        remaining_lives = remaining_lives-1
        soulation=int(input("guess the number:"))
        if soulation > the_number :
            print("too high")
        elif soulation < the_number:
            print("too low")
        elif soulation == the_number:
            print("right number you won")
            break

def easy():
    the_number = random.choice(numbers_list)
    remaining_lives = 10
    for j in range(10):
        print(f"remaining lives is {remaining_lives}")
        remaining_lives = remaining_lives-1
        soulation = int(input("guess the number:"))
        if soulation > the_number:
            print("too high")
        elif soulation < the_number:
            print("too low")
        elif soulation == the_number:
            print("right number you won")
            break
        
print(logo)
print("\n welcome to the game")
print("\n guess the number from 0 to 100 ???")
q1="\n what level do you want to play( easy / hard )"
level = str(input(f"{q1}"))

if level=="easy":
    easy()
elif level=="hard":
    hard()