# Q1.1
def get_positive_decimal():
    while True:
        try:
            # Ask for input
            num = float(input("Input a decimal: "))
            # Check if input is positive
            if num > 0:
                return num
            else:
                print("Please input a positive decimal!")
        # Check if input is decimal
        except ValueError:
            print("Please input a positive decimal!")

# Print output
print(get_positive_decimal())
