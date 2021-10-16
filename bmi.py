height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = float(weight) / (float(height) ** 2)
your_bmi = round(BMI, 2)
print(f"Your BMI is {your_bmi}")
