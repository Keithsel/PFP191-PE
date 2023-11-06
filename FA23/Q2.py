# Q2.1
def get_average_score(scores, weights):
    # Check if length of scores and weights are the same
    if len(scores) != len(weights):
        raise ValueError("Length of scores and weights must be the same!")
    # Calculate average score
    return sum([scores[i] * weights[i] for i in range(len(scores))]) / sum(weights)

# Print output if needed
# print(get_average_score((10,5,6,7),(1,2,3,4)))

# Q2.2
def get_score_report():
    # Define subjects and weights
    subjects = ("CSI105", "MAD101", "MAE101", "PFP191")
    weights = (3, 3, 3, 3)
    while True:
        # Ask for student name
        name = input("Please input student name: ")
        # Ask for scores
        scores = []
        for subject in subjects:
            while True:
                try:
                    score = float(input(f"Please input score of {subject}: "))
                    # Check if score is in range
                    if 0 <= score <= 10:
                        scores.append(score)
                        break
                    else:
                        print("Score must be in range 0 - 10!")
                except ValueError:
                    print("Please input a number!")
        # Calculate average score
        average_score = get_average_score(scores, weights)
        # Write to file
        with open("score_report.txt", "a") as file:
            file.write(f"{name},")
            for i in range(len(subjects)):
                file.write(f"{scores[i]},")
            file.write(f"{average_score}\n")
        # Ask if user wants to continue
        while True:
            choice = input("Do you want to continue? (y/n): ")
            if choice == "y" or choice == "":
                break
            elif choice == "n":
                return
            else:
                print("Invalid input. Please input y or n!")

get_score_report()
