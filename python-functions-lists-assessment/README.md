# Python Functions, Strings & Lists — Assessment

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Functions%20%7C%20Strings%20%7C%20Lists-0A7B83)

## 📌 Overview

This assessment contains two console programs written in Python 3:

| # | Program | File | Topics |
|:-:|---|---|---|
| 1 | Student Result Card Generator | [`result_card_generator.py`](./result_card_generator.py) | Functions, parameters, `return`, string manipulation |
| 2 | Class Marks Analyzer | [`class_marks_analyzer.py`](./class_marks_analyzer.py) | Lists, `append()`, `len()`, `sum()`, `max()`, `min()`, `sorted()`, loops |

Both programs validate every input and keep asking until the value is valid, so bad input never crashes them.

---

## 🧾 Task 1: Student Result Card Generator

Builds a result card for one student.

**What it does**
1. Asks for the student's name, roll number, and marks in five subjects (English, Urdu, Mathematics, Physics, Computer Science).
2. Cleans the name with `.strip()` and `.title()` (for example, `"  aLi   ahMED "` becomes `"Ali Ahmed"`).
3. Accepts a roll number only if it contains digits, checked with `.isdigit()`.
4. Accepts marks only if they are whole numbers from 0 to 100.
5. Works out the total, the percentage (2 decimal places) and the grade.
6. **Special rule:** if any subject is below 40, the final result is **Fail**, whatever the overall percentage. The card shows which subject(s) caused it.

**Grading criteria**

| Percentage | Grade |
|---|:-:|
| 90 and above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | Fail |

**Functions**

| Function | Purpose |
|---|---|
| `format_name(name)` | Removes extra spaces and capitalises each word |
| `get_student_name()` | Asks until a valid name (letters and spaces) is entered |
| `get_roll_number()` | Asks until the roll number contains digits only |
| `get_valid_marks(subject)` | Asks until the marks are a whole number from 0 to 100 |
| `calculate_percentage(total, max_total)` | Returns the percentage |
| `get_grade(percentage)` | Returns the letter grade from the table above |
| `get_failed_subjects(subject_marks)` | Returns the subjects scored below 40 |
| `print_result_card(...)` | Prints the formatted card using f-strings |
| `main()` | Runs the whole program |

---

## 📊 Task 2: Class Marks Analyzer

Analyses the results of a whole class.

**What it does**
1. Asks how many students are in the class.
2. Stores the data in two parallel lists, `student_names = []` and `student_marks = []`, filled with `.append()`.
3. Validates each mark (0–100) and asks again if it is invalid.
4. Reports:
   - the class average
   - the highest marks and **all** students who got them, so ties are handled
   - the lowest marks and all students who got them
   - how many students passed (50 or above) and failed (below 50)
   - the students who scored above the class average
   - all marks sorted from highest to lowest, with rank and Pass/Fail

**Functions**

| Function | Purpose |
|---|---|
| `get_student_count()` | Asks until the class size is a whole number above 0 |
| `get_student_name(position)` | Asks until a non-empty name is entered |
| `get_valid_marks(student_name)` | Asks until the marks are a whole number from 0 to 100 |
| `calculate_average(marks_list)` | Returns `sum() / len()` |
| `find_students_with_marks(names, marks_list, target)` | Returns every student with the given marks |
| `count_pass_fail(marks_list)` | Returns the pass and fail counts |
| `get_above_average(names, marks_list, average)` | Returns the students above the average |
| `sort_by_marks(names, marks_list)` | Returns `(name, marks)` pairs sorted highest first |
| `print_report(...)` | Prints the full class report |
| `main()` | Runs the whole program |

---

## 🧠 Python Concepts Used

| Concept | Where it is used |
|---|---|
| `def`, parameters, `return` | Every task is split into small, reusable functions |
| `while True` + `return` | Asking again until the input is valid |
| `try` / `except ValueError` | Handling non-numeric input such as `abc` |
| `.strip()`, `.title()`, `.split()`, `.join()` | Cleaning names |
| `.isdigit()`, `.isalpha()` | Validating the roll number and name |
| `if` / `elif` / `else` | Grade calculation and pass/fail checks |
| `for` loops, `range()`, `enumerate()` | Going through subjects and students |
| Lists and `.append()` | `student_names`, `student_marks` |
| `len()`, `sum()`, `max()`, `min()` | Class statistics |
| `sorted()` with `zip()` and `key=` | Ranking students by marks |
| Dictionary | Storing subject → marks in Task 1 |
| f-strings with `:.2f`, `:<`, `:>`, `:^` | Aligned, formatted output |
| `if __name__ == "__main__":` | Runs `main()` only when the file is executed directly |

---

## ▶️ How to Run

**Requirement:** Python 3.x. No extra packages are needed.

```bash
cd python-functions-lists-assessment

# Task 1
python result_card_generator.py

# Task 2
python class_marks_analyzer.py
```

> On macOS or Linux, use `python3` instead of `python`.

---

## 🧪 Sample Input & Output

### Task 1: Pass

```text
Enter student name:   aLi   ahMED khan
Enter roll number: 12a
  Invalid roll number! Use digits only (e.g. 1024).

Enter roll number: 1024
Enter marks for English (0-100): 85
Enter marks for Urdu (0-100): 78
Enter marks for Mathematics (0-100): 92
Enter marks for Physics (0-100): 88
Enter marks for Computer Science (0-100): 95

============================================
            STUDENT RESULT CARD
============================================
Name          : Ali Ahmed Khan
Roll Number   : 1024
--------------------------------------------
Subject                                Marks
--------------------------------------------
English                             85 / 100
Urdu                                78 / 100
Mathematics                         92 / 100
Physics                             88 / 100
Computer Science                    95 / 100
--------------------------------------------
Total Marks                        438 / 500
Percentage                            87.60%
Grade                                      A
Final Status                            Pass
============================================
```

### Task 1: Fail because one subject is below 40 (overall 81.60%)

```text
Enter marks for English (0-100): abc
  Invalid input! Please enter a whole number.

Enter marks for English (0-100): 150
  Marks must be between 0 and 100.
...
--------------------------------------------
Total Marks                        408 / 500
Percentage                            81.60%
Grade                                   Fail
Final Status                            Fail
============================================
Note: Scored below 40 in: Urdu
============================================
```

### Task 2

```text
How many students are in the class? 5

Enter name of student 1: ali
Enter marks for Ali (0-100): 85

Enter name of student 2: sara
Enter marks for Sara (0-100): 110
  Marks must be between 0 and 100. Please try again.
Enter marks for Sara (0-100): 92
...

============================================
          CLASS PERFORMANCE REPORT
============================================
Total Students        : 5
Class Average         : 68.80
Highest Marks         : 92 (Sara, Fatima)
Lowest Marks          : 30 (Usman)
Passed (50 or above)  : 3
Failed (below 50)     : 2

--------------------------------------------
Students above class average (68.80):
--------------------------------------------
  Ali                             85
  Sara                            92
  Fatima                          92

--------------------------------------------
Marks sorted from highest to lowest:
--------------------------------------------
   1. Sara                      92   Pass
   2. Fatima                    92   Pass
   3. Ali                       85   Pass
   4. Ahmed                     45   Fail
   5. Usman                     30   Fail
============================================
```

---

## ✅ Test Scenarios Checked

| Program | Scenario | Result |
|---|---|---|
| Task 1 | All subjects passed, 87.60% | Grade A, Pass |
| Task 1 | 81.60% overall but Urdu = 35 | Fail, with the reason shown |
| Task 1 | All subjects 40+, but 45.20% overall | Fail |
| Task 1 | Name `123`, roll number `12a`, marks `abc` / `150` / `-5` | Rejected and asked again |
| Task 2 | 5 students with a tie for the highest marks | Both top students listed |
| Task 2 | Class size `abc` / `0`, empty name, marks `110` | Rejected and asked again |
| Task 2 | 1 student (nobody above the average) | Shows "No student scored above the average." |
