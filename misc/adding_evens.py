total = 0
for even in range(2, 101, 2):
    total += even
print(total)

# or can do

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
    print(total2)
