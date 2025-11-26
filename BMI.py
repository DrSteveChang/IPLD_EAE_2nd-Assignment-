# BMI Calculator

# Ask the user for height (in meters)
height = float(input("Enter your height in meters: "))

# Ask the user for weight (in kilograms)
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the result
print(f"\nYour BMI is: {bmi:.2f}")

# Interpret the result
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
