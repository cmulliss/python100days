# dictionaries, {key: value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# use [] and the key to get the definition
print(programming_dictionary["Bug"])

# to add an entry, use [] and = ("")
programming_dictionary["Loop"] = ("The action of doing something over and over again.",)
print(programming_dictionary)


# can be helpful to create an empty dictionary to start
# empty_dict = {}

# and can wipe an existing dictionary
# programming_dictionary = {}

# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
