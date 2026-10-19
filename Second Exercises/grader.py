def main():
    grade = input("What is your grade? (0-100) \n")
    print(grader(grade))
def grader(grade):
    if not grade.strip(".").isdigit():
        letter = "This is not a number"
    else:
        grade = int(grade)
        if grade >= 90:
            letter = "A"
        elif grade>= 80:
            letter = "B"
        elif grade >= 70:
            letter = "C"
        elif grade >= 60:
            letter = "D"
        else:
            letter = "F"
    return letter

main()