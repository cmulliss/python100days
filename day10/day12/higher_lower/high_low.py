# display art

# import randint
from random import randint

# import data
import /Users/cherry/repos/python100days/day10/day12/higher_lower/game_data.py


# generate a random account from game data

# format the account data into a printable format

# ask user for a guess

# check if user is correct


# generate a random number

rand1 = randint(0, 10)
print(rand1)
# generate a second random number
rand2 = randint(0, 10)
print(rand2)

# compare the 2
if rand1 > rand2:
    print("You win")
elif rand1 == rand2:
    print("A draw")
else:
    print("Sorry, you lose")
