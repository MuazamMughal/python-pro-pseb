# Task 2: Class Marks Analyzer
# Topics: Lists (create, append(), len(), sum(), max(), min(), sorted()) and Loops
#
# The program collects names and marks for a whole class, stores them in
# two parallel lists, and prints a performance report: average, highest,
# lowest, pass/fail counts, above-average students and a ranked list.

PASS_MARKS = 50
MAX_MARKS = 100
LINE = "=" * 44


# Keep asking until the number of students is a whole number greater than 0.
def get_student_count():
    while True:
        try:
            count = int(input("How many students are in the class? ").strip())
        except ValueError:
            print("  Invalid input! Please enter a whole number.\n")
            continue

        if count > 0:
            return count
        print("  There must be at least 1 student.\n")


# Keep asking until a non-empty name is entered, then return it cleaned up.
def get_student_name(position):
    while True:
        name = input(f"\nEnter name of student {position}: ").strip().title()
        if name:
            return name
        print("  Name cannot be empty.")


# Keep asking until the marks are a whole number between 0 and 100.
def get_valid_marks(student_name):
    while True:
        try:
            marks = int(input(f"Enter marks for {student_name} (0-{MAX_MARKS}): ").strip())
        except ValueError:
            print("  Invalid input! Please enter a whole number.")
            continue

        if 0 <= marks <= MAX_MARKS:
            return marks
        print(f"  Marks must be between 0 and {MAX_MARKS}. Please try again.")


# Return the average of a list of marks.
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)


# Return the names of every student whose marks equal the target value.
def find_students_with_marks(names, marks_list, target):
    matching_names = []
    for index in range(len(marks_list)):
        if marks_list[index] == target:
            matching_names.append(names[index])
    return matching_names


# Return how many students passed and how many failed as a pair (passed, failed).
def count_pass_fail(marks_list):
    passed = 0
    failed = 0
    for marks in marks_list:
        if marks >= PASS_MARKS:
            passed += 1
        else:
            failed += 1
    return passed, failed


# Return a list of (name, marks) pairs for students scoring above the average.
def get_above_average(names, marks_list, average):
    above = []
    for index in range(len(marks_list)):
        if marks_list[index] > average:
            above.append((names[index], marks_list[index]))
    return above


# Return (name, marks) pairs sorted from highest to lowest marks.
def sort_by_marks(names, marks_list):
    # zip() pairs each name with its marks: [("Ali", 85), ("Sara", 92), ...]
    # key=lambda pair: pair[1] tells sorted() to compare by the marks part
    # reverse=True puts the highest marks first
    return sorted(zip(names, marks_list), key=lambda pair: pair[1], reverse=True)


# Print the full class report from the two lists.
def print_report(student_names, student_marks):
    average = calculate_average(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)
    top_students = find_students_with_marks(student_names, student_marks, highest)
    bottom_students = find_students_with_marks(student_names, student_marks, lowest)
    passed, failed = count_pass_fail(student_marks)
    above_average = get_above_average(student_names, student_marks, average)
    ranking = sort_by_marks(student_names, student_marks)

    print("\n" + LINE)
    print(f"{'CLASS PERFORMANCE REPORT':^44}")
    print(LINE)
    print(f"{'Total Students':<22}: {len(student_marks)}")
    print(f"{'Class Average':<22}: {average:.2f}")
    print(f"{'Highest Marks':<22}: {highest} ({', '.join(top_students)})")
    print(f"{'Lowest Marks':<22}: {lowest} ({', '.join(bottom_students)})")
    print(f"{'Passed (50 or above)':<22}: {passed}")
    print(f"{'Failed (below 50)':<22}: {failed}")

    print("\n" + "-" * 44)
    print(f"Students above class average ({average:.2f}):")
    print("-" * 44)
    if above_average:
        for name, marks in above_average:
            print(f"  {name:<28}{marks:>6}")
    else:
        # Happens when everyone has the same marks
        print("  No student scored above the average.")

    print("\n" + "-" * 44)
    print("Marks sorted from highest to lowest:")
    print("-" * 44)
    # enumerate(..., start=1) gives the rank number 1, 2, 3 ...
    for rank, (name, marks) in enumerate(ranking, start=1):
        status = "Pass" if marks >= PASS_MARKS else "Fail"
        print(f"  {rank:>2}. {name:<22}{marks:>6}   {status}")
    print(LINE)


# Run the program: collect names and marks into lists, then print the report.
def main():
    print(LINE)
    print(f"{'CLASS MARKS ANALYZER':^44}")
    print(LINE)

    # Two parallel lists: student_names[i] belongs with student_marks[i]
    student_names = []
    student_marks = []

    count = get_student_count()

    for position in range(1, count + 1):
        name = get_student_name(position)
        marks = get_valid_marks(name)
        student_names.append(name)
        student_marks.append(marks)

    print_report(student_names, student_marks)


# Only run main() when this file is executed directly (not imported)
if __name__ == "__main__":
    main()
