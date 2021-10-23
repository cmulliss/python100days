import random

names_string = input("Give me everybody's names, separated by a comma. ")
# will create a list of the names entered
names = names_string.split(", ")
print(names)
who_pays = random.choice(names)
print(f"{who_pays} is going to buy the meal today.")

# or can do

# find number of names, then use random generator, allowing for starting at 0, so -1
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_pays = names[random_choice]
print(f"{person_who_pays} is going to buy the meal today.")
