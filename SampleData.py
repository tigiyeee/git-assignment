print("Intro to Python")


height = input("Enter your height in metres: ")
weight = input("Enter your weight in kilograms: ")

h = float(height)
w = float(weight)

bmi = w / (h ** 2)

print("Your BMI is:", round(bmi, 2))
