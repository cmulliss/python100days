############DEBUGGING#####################

# # Describe Problem
# range goes to penultimate number so need to have 21 as upper limit
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")


# my_function()

# # Reproduce the Bug
# similar to above, the range is up to 5, for 6th place
# from random import randint

# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = 5
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1946 and year < 1964:
#     print("You are a baby boomer")
# elif year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# else:
#     print("You don't fit into any of these silly categories!")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print(f"You are too young to drive at {age}")

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
