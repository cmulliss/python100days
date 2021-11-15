import string
import random

# characters to choose from
characters = list(
    string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
)


def gen_random_pwd():
    length = int(input("How many characters long do you want your password? "))

    # choosing random chars from list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # shuffling password
    random.shuffle(password)

    # convert list to string and print
    print("".join(password))


# invoke fn
gen_random_pwd()
