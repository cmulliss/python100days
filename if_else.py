print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        print("Adult tickets are $12")
        bill = 12
    # same indent as block
    photo = input("Do you want a photo taken? (Y or N) ").upper()
    # if yes, how to add $3 to their bill?
    if photo == "Y":
        bill += 3
    print(f"Your total bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")
