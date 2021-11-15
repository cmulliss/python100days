height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

your_bmi = round(weight / height ** 2)

if your_bmi <= 18.5:
    print(f"Your BMI is {your_bmi}. You are underweight")
elif your_bmi <= 25:
    print(f"Your BMI is {your_bmi}. You are in the normal weight range")
elif your_bmi < 30:
    print(f"Your BMI is {your_bmi}. You are slightly overweight")
elif your_bmi < 35:
    print(f"Your BMI is {your_bmi}. You are obese")
else:
    print(f"Your BMI is {your_bmi}. You are clinically obese")
