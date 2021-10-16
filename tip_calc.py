print("welcome to the tip calcultor. ")
total_bill = float(input("what was the total bill?\n"))
number_people = int(input("How many diners are sharing the bill\n"))
share = total_bill / number_people
print(f"Each diner will pay £{share}")
