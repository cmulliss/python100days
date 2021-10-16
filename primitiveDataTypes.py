# strings

print(len("Hello"))

print("Hello"[4])
# gives 0

# integers, can use _ and is ignored
print(1234_567)  # gives 1234567

# Float, floating point numbers

# Boolean

street = "Abbey Road"
print(street[4] + street[7])  # yo

# type checking, for when not sure what th type is.

num_char = len(input("What is your name? "))
print(type(num_char))
# str(num_char)
print(f"Your name has {num_char} characters")

# type casting

a = str(123)
print(type(a))

b = int(123)
print(type(b))

print(70 + float("20.4"))
