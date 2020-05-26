# Write your code here
import random


# calculate and store score with name key in rating dict
def write_rating(cur_name, cur_score):
    if cur_name in rating:
        rating[cur_name] = int(rating[cur_name]) + cur_score
    else:
        rating[cur_name] = cur_score


# empty dicts
# rating name:score
rating = {}
# game rules
# who beats key
win = {}
# key: key
draw = {}
# who loses key
lose = {}
# start
print("Enter your name: ", end="")
users_name = input()
print("Hello, {}".format(users_name))
options = input().split(",")
# if options id omitted fill with default options and rules
if options == ['']:
    items = ["rock", "scissors", "paper"]
    win = dict(scissors=["rock"], paper=["scissors"], rock=["paper"])
    draw = dict(scissors=["scissors"], paper=["paper"], rock=["rock"])
    lose = dict(scissors=["paper"], paper=["rock"], rock=["scissors"])
# fill with chosen options
else:
    items = options
    for i in items:
        items_minus_i = items[items.index(i) + 1:]
        items_minus_i.extend(items[:items.index(i)])
        win[i] = items_minus_i[:len(items_minus_i) // 2]
        draw[i] = i
        lose[i] = items_minus_i[len(items_minus_i) // 2:]
print("Okay, let's start")
# read rating file
rating_file = open("rating.txt", "r+")
for s in rating_file:
    name, score = s.split()
    rating[name] = int(score)
rating_file.close()
computers_choice = random.choice(items)
users_choice = input()
# main loop
while not users_choice == "!exit":
    # if choice is in options
    if users_choice in items:
        # users choice in who beats key=computers choice
        if users_choice in win[computers_choice]:
            print("Well done. Computer chose {} and failed".format(computers_choice))
            write_rating(users_name, 100)
        # users choice = computes choice
        elif users_choice in draw[computers_choice]:
            print("There is a draw ({})".format(computers_choice))
            write_rating(users_name, 50)
        # users choice in who loses key=computers choice
        elif users_choice in lose[computers_choice]:
            print("Sorry, but computer chose {}".format(computers_choice))
# show rating command
    elif users_choice == "!rating":
        print("Your rating: ", end="")
        if users_name in rating:
            print(rating[users_name])
        else:
            print("0")
# invalid choice
    else:
        print("Invalid input")
# continue game
    computers_choice = random.choice(items)
    users_choice = input()
# writing new rating in file after game ends and exit
rating_file = open("rating.txt", "w")
for s in rating:
    print(s, rating[s], file=rating_file)
rating_file.close()
print("Bye!")
