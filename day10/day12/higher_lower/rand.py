# import randint
from random import randint

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
