# bmi_calculator.py

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"BMI: {bmi:.2f} (Underweight)"
    elif 18.5 <= bmi < 24.9:
        return f"BMI: {bmi:.2f} (Normal weight)"
    elif 25 <= bmi < 29.9:
        return f"BMI: {bmi:.2f} (Overweight)"
    else:
        return f"BMI: {bmi:.2f} (Obesity)"

# Sample usage
print(calculate_bmi(70, 1.75))  # Weight in kg, height in meters
