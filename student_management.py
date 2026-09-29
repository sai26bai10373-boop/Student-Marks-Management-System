import csv
import os

file_name = "students.csv"

# Function to create CSV file if not exists
def setup_file():
    if not os.path.exists(file_name):
        f = open(file_name, "w", newline="")
        writer = csv.writer(f)
        writer.writerow(["Roll No", "Name", "Python", "Maths", "English", "Total", "Percentage", "Grade"])
        f.close()

# Function to calculate grade
def get_grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"

# Function to add student record
def add_student():
    roll = input("Enter roll no: ")
    name = input("Enter name: ")
    
    p = float(input("Enter Python marks: "))
    m = float(input("Enter Maths marks: "))
    e = float(input("Enter English marks: "))
    
    # Check valid marks
    if p < 0 or p > 100 or m < 0 or m > 100 or e < 0 or e > 100:
        print("Marks should be between 0 and 100!")
        return

    total = p + m + e
    per = round(total / 3, 2)
    grade = get_grade(per)

    f = open(file_name, "a", newline="")
    writer = csv.writer(f)
    writer.writerow([roll, name, p, m, e, total, per, grade])
    f.close()
    
    print("Student added successfully!")

# Function to view all students
def view_all():
    if not os.path.exists(file_name):
        print("File not found.")
        return

    f = open(file_name, "r")
    reader = csv.reader(f)
    data = list(reader)
    f.close()

    if len(data) <= 1:
        print("No records found.")
        return

    print("\n--- ALL STUDENTS ---")
    for row in data:
        print(row)

# Function to search a student by roll number
def search_student():
    roll = input("Enter roll no to search: ")
    found = False

    f = open(file_name, "r")
    reader = csv.reader(f)
    next(reader)  # Skip header

    for row in reader:
        if row[0] == roll:
            print("\nStudent Found:")
            print("Name       :", row[1])
            print("Python     :", row[2])
            print("Maths      :", row[3])
            print("English    :", row[4])
            print("Total      :", row[5])
            print("Percentage :", row[6])
            print("Grade      :", row[7])
            found = True
            break
    f.close()

    if not found:
        print("Student not found.")

# Function for class summary
def summary():
    f = open(file_name, "r")
    reader = csv.reader(f)
    next(reader)  # Skip header

    percentages = []

    for row in reader:
        percentages.append(float(row[6]))
    f.close()

    if len(percentages) == 0:
        print("No records available.")
        return

    avg = sum(percentages) / len(percentages)
    highest = max(percentages)
    lowest = min(percentages)

    print("\n--- CLASS SUMMARY ---")
    print("Total Students :", len(percentages))
    print("Class Average  :", round(avg, 2))
    print("Highest Marks  :", highest)
    print("Lowest Marks   :", lowest)

# Main program
setup_file()

while True:
    print("\n=== STUDENT MENU ===")
    print("1. Add Student")
    print("2. View All")
    print("3. Search Student")
    print("4. Class Summary")
    print("5. Exit")
    
    ch = input("Enter choice (1-5): ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_all()
    elif ch == "3":
        search_student()
    elif ch == "4":
        summary()
    elif ch == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice, please try again.")