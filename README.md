# 🐍 Python Pro — PSEB Python Web & AI Engineer Course

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Course](https://img.shields.io/badge/Course-PSEB%20Python%20Web%20%26%20AI%20Engineer-0A7B83)
![Status](https://img.shields.io/badge/Status-In%20Progress-brightgreen)

This repository holds all my assignments, class exercises and practice projects from the **PSEB Python Web & AI Engineer** course. Every topic gets its own folder, and each folder has its own code and README.

The aim is to build a clear, step-by-step record of my progress, from Python fundamentals through web development to AI engineering.

---

## 📚 Table of Contents

- [Projects](#-projects)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Learning Roadmap](#-learning-roadmap)
- [Skills Practiced So Far](#-skills-practiced-so-far)
- [How New Assignments Are Added](#-how-new-assignments-are-added)

---

## 🚀 Projects

| # | Project | Topic | Key Concepts | Run |
|:-:|---|---|---|---|
| 1 | [Smart Canteen Discount System](./python-conditionals-smart-canteen) | Conditional statements | `if` / `elif` / `else`, comparison operators, percentages, f-strings | `python smart_canteen_discount.py` |
| 2 | [Smart Electricity Bill Calculator](./python-loops-electricity-bill-calculator) | Loops | `for` loops, `range()`, accumulators, `continue`, tiered billing | `python smart_electricity_bill.py` |
| 3 | [Functions, Strings & Lists Assessment](./python-functions-lists-assessment) | Functions, strings, lists | `def` / `return`, `.strip()` / `.title()` / `.isdigit()`, `append()`, `sum()`, `max()`, `min()`, `sorted()` | `python result_card_generator.py`<br>`python class_marks_analyzer.py` |

### 1. Smart Canteen Discount System
A college canteen gives a discount based on the size of the bill (0%, 5%, 10% or 20%). The program chooses the right tier with an `if` / `elif` / `else` chain, then prints a bill summary showing the discount and the final amount to pay.

➡️ [View project](./python-conditionals-smart-canteen)

### 2. Smart Electricity Bill Calculator
An electricity company works out monthly bills for several households using progressive rates (Rs. 10 / 15 / 20 per unit). A `for` loop handles each household, invalid readings are skipped with `continue`, and an accumulator adds up the total revenue for the final report.

➡️ [View project](./python-loops-electricity-bill-calculator)

### 3. Functions, Strings & Lists Assessment
This assessment has two programs. The **Student Result Card Generator** validates a student's details, works out the percentage and grade, and fails a student who scores below 40 in any subject. The **Class Marks Analyzer** stores a whole class in two lists and reports the average, the top and bottom students (ties included), pass/fail counts, the students above the average, and a ranked list.

➡️ [View project](./python-functions-lists-assessment)

---

## 🗂 Repository Structure

```text
python-pro-pseb/
├── README.md                                   ← you are here
├── python-conditionals-smart-canteen/
│   ├── README.md
│   └── smart_canteen_discount.py
├── python-loops-electricity-bill-calculator/
│   ├── README.md
│   └── smart_electricity_bill.py
└── python-functions-lists-assessment/
    ├── README.md
    ├── result_card_generator.py
    └── class_marks_analyzer.py
```

---

## 🛠 Getting Started

**Requirements:** Python 3.x. The projects so far use only the standard library, so there is nothing to install.

```bash
# Clone the repository
git clone https://github.com/MuazamMughal/python-pro-pseb.git
cd python-pro-pseb

# Run any project
cd python-loops-electricity-bill-calculator
python smart_electricity_bill.py
```

> On macOS or Linux you may need to use `python3` instead of `python`.

---

## 🗺 Learning Roadmap

| Stage | Area | Status |
|---|---|:-:|
| 1 | Python fundamentals: variables, input/output, operators | ✅ |
| 2 | Conditional statements | ✅ |
| 3 | Loops | ✅ |
| 4 | Functions, strings and lists | ✅ |
| 5 | File handling, error handling and OOP | ⏳ |
| 6 | Web development with Python | ⏳ |
| 7 | Databases and APIs | ⏳ |
| 8 | AI / ML and LLM-powered applications | ⏳ |

✅ Completed  ⏳ Upcoming

---

## 🧠 Skills Practiced So Far

- Taking user input with `input()` and converting it with `int()` / `float()`
- Making decisions with `if`, `elif` and `else`
- Repeating work with `for` loops and `range()`
- Keeping running totals with accumulators
- Skipping invalid data with `continue`
- Turning real-world business rules (discounts, tiered tariffs) into code
- Formatting clean console output with f-strings
- Writing reusable functions with parameters and `return`
- Cleaning and validating text with `.strip()`, `.title()`, `.isdigit()` and `.isalpha()`
- Asking again after invalid input with `while` loops and `try` / `except`
- Storing data in lists and analysing it with `len()`, `sum()`, `max()`, `min()` and `sorted()`

---

## ➕ How New Assignments Are Added

Each new assignment follows the same pattern:

1. A new folder named `python-<topic>-<project-name>`
2. The Python source file(s) inside it
3. A `README.md` covering the scenario, concepts, how to run it and sample output
4. A new row in the **Projects** table above

---

## 👤 Author

**Muazam Mughal**
Student, PSEB Python Web & AI Engineer course
GitHub: [@MuazamMughal](https://github.com/MuazamMughal)

---

⭐ If you find these examples helpful while learning Python, feel free to star the repo!
