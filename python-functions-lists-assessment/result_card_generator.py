# Task 1: Student Result Card Generator
# Topics: Functions (def, parameters, return) and String Manipulation
#
# The program asks for one student's name, roll number and marks in
# five subjects, validates every input, then prints a formatted result
# card with total, percentage, grade and final Pass/Fail status.

# ---------------- Settings used across the program ----------------
SUBJECTS = ["English", "Urdu", "Mathematics", "Physics", "Computer Science"]
MAX_MARKS_PER_SUBJECT = 100
MIN_PASS_MARKS_PER_SUBJECT = 40   # below this in ANY subject = Fail
CARD_WIDTH = 44                   # width of the printed result card


# Clean a name: remove extra spaces and capitalise every word.
def format_name(name):
    cleaned = name.strip()                 # remove spaces at both ends
    cleaned = " ".join(cleaned.split())    # collapse double spaces inside
    return cleaned.title()                 # "ali  KHAN" -> "Ali Khan"


# Keep asking until the user enters a valid name (letters and spaces only).
def get_student_name():
    while True:
        name = format_name(input("Enter student name: "))
        # Remove spaces before checking, because "Ali Khan".isalpha() is False
        if name and name.replace(" ", "").isalpha():
            return name
        print("  Invalid name! Use letters and spaces only.\n")


# Keep asking until the roll number contains digits only.
def get_roll_number():
    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            return roll_number
        print("  Invalid roll number! Use digits only (e.g. 1024).\n")


# Keep asking until the marks for one subject are a whole number from 0 to 100.
def get_valid_marks(subject):
    while True:
        user_input = input(f"Enter marks for {subject} (0-{MAX_MARKS_PER_SUBJECT}): ").strip()

        # try/except catches text such as "abc" that int() cannot convert
        try:
            marks = int(user_input)
        except ValueError:
            print("  Invalid input! Please enter a whole number.\n")
            continue

        if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
            return marks
        print(f"  Marks must be between 0 and {MAX_MARKS_PER_SUBJECT}.\n")


# Return the percentage of obtained marks out of the maximum marks.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# Return the letter grade for a percentage using the grading table.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Return a list of subjects in which the student scored below the pass mark.
def get_failed_subjects(subject_marks):
    failed = []
    for subject, marks in subject_marks.items():
        if marks < MIN_PASS_MARKS_PER_SUBJECT:
            failed.append(subject)
    return failed


# Print the complete result card using f-strings.
def print_result_card(name, roll_number, subject_marks, total, max_total,
                      percentage, grade, status, failed_subjects):
    line = "=" * CARD_WIDTH
    divider = "-" * CARD_WIDTH

    print("\n" + line)
    print(f"{'STUDENT RESULT CARD':^{CARD_WIDTH}}")   # ^ centres the text
    print(line)
    print(f"{'Name':<14}: {name}")
    print(f"{'Roll Number':<14}: {roll_number}")
    print(divider)
    print(f"{'Subject':<28}{'Marks':>16}")
    print(divider)
    for subject, marks in subject_marks.items():
        print(f"{subject:<28}{marks:>10} / {MAX_MARKS_PER_SUBJECT}")
    print(divider)
    print(f"{'Total Marks':<28}{total:>10} / {max_total}")
    print(f"{'Percentage':<28}{percentage:>15.2f}%")
    print(f"{'Grade':<28}{grade:>16}")
    print(f"{'Final Status':<28}{status:>16}")
    print(line)

    # Explain WHY the student failed when it is because of a single subject
    if failed_subjects:
        print(f"Note: Scored below {MIN_PASS_MARKS_PER_SUBJECT} in: {', '.join(failed_subjects)}")
        print(line)


# Run the program: collect input, calculate results and print the card.
def main():
    print("=" * CARD_WIDTH)
    print(f"{'RESULT CARD GENERATOR':^{CARD_WIDTH}}")
    print("=" * CARD_WIDTH)

    name = get_student_name()
    roll_number = get_roll_number()

    # Store marks in a dictionary: {"English": 85, "Urdu": 78, ...}
    subject_marks = {}
    for subject in SUBJECTS:
        subject_marks[subject] = get_valid_marks(subject)

    total = sum(subject_marks.values())
    max_total = MAX_MARKS_PER_SUBJECT * len(SUBJECTS)
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    failed_subjects = get_failed_subjects(subject_marks)

    # Special rule: below 40 in ANY subject means Fail,
    # even if the overall percentage is high.
    if failed_subjects:
        grade = "Fail"

    status = "Fail" if grade == "Fail" else "Pass"

    print_result_card(name, roll_number, subject_marks, total, max_total,
                      percentage, grade, status, failed_subjects)


# Only run main() when this file is executed directly (not imported)
if __name__ == "__main__":
    main()
