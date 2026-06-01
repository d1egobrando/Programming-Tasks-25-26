def grade_calc(score):
    if score >= 80 and score <= 100:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "D"

percentage = int(input("Enter your percentage grade: "))

grade = grade_calc(percentage)

print("Your grade is:", grade)
