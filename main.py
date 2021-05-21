import random
from game_data import data
from art import logo,vs
from replit import clear



def check(guess,follower1,follower2):
    """""function to check who has more followers"""
    if follower1 > follower2:
        return guess == "a"
    else :
        return guess == "b"
ran2 = random.randint(0,49)
score =0
game_should_continue = True
print(logo)

while game_should_continue:
    """"For Repeating the game"""
    ran1 = ran2
    ran2 = random.randint(0,49)
    while ran1 == ran2:
        ran2 = random.randint(0,49)

    item1 = data[ran1]
    item2 = data[ran2]
    a_list = []
    b_list = []
    for key in item1 :
        a_list.append(item1[key])
    for key in item2:
        b_list.append(item2[key])


    print(f"Compare A: {a_list[0]}, a {a_list[2]}, from {a_list[3]}.")
    print(vs)
    print(f"Against B: {b_list[0]}, a {b_list[2]}, from {b_list[3]}.")


    follower1 = a_list[1]
    follower2 = b_list[1]
    guess=input("Who has more followers? Type 'A' or 'B' : ").lower()

    is_correct = check(guess,follower1,follower2)
    clear()
    print(logo)
    if is_correct == True:
        score+=1
        print(f"You are correct. Current score {score}")
    else:
        game_should_continue = False
        print(f"You are Wrong. Final score {score}")