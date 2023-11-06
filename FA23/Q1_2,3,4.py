# Q1.2
def lb_to_kg(weight):
    return weight * 0.453592

# # Print output if needed
# print(lb_to_kg(1))

# Q1.3
def inch_to_m(height):
    return height * 2.54 / 100

# Print output if needed
# print(inch_to_m(1))

# Q1.4
def get_bmi():
    # Define BMI classification ranges and labels
    bmi_ranges = {
        (0, 16): "severe thinness",
        (16, 17): "moderate thinness",
        (17, 18.5): "mild thinness",
        (18.5, 25): "normal",
        (25, 30): "overweight",
        (30, 35): "obese class I",
        (35, 40): "obese class II",
        (40, float("inf")): "obese class III"
    }
    # Ask for input
    print(f"Do you want to input your weight and height in SI units or imperial units: \n1. SI units (default)\n2. Imperial units\n")
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice == "" or choice == "1":
                # Ask for input
                weight = float(input("Enter your weight in kg: "))
                height = float(input("Enter your height in m: "))
                break
            elif choice == "2":
                # Ask for input
                weight = float(input("Enter your weight in lb: "))
                height = float(input("Enter your height in inch: "))
                # Convert to SI units
                weight = lb_to_kg(weight)
                height = inch_to_m(height)
                break
            else:
                print("Invalid input. Please input 1 or 2!")
        except ValueError:
            print("Invalid input. Please input 1 or 2!")
    # Calculate BMI
    bmi = weight / height ** 2
    # Classify BMI
    for bmi_range, label in bmi_ranges.items():
        if bmi >= bmi_range[0] and bmi < bmi_range[1]:
            classification = label
            break
    # Print output
    print(f"Your BMI is {bmi:.1f}, your class is {classification}")

get_bmi()
