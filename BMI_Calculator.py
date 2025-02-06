def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
