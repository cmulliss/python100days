two_digit_number = input("Type a 2 digit no: ")

print(type(two_digit_number))
# gives str so convert to ints

# one = two_digit_number[0]
# two = two_digit_number[1]

# could have converted above:

one = int(two_digit_number[0])
two = int(two_digit_number[1])

# result = int(one) + int(two)
print(one + two)
