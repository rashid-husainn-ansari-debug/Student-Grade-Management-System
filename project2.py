# Initialising dictionary
student_grades = {}

# Add a new student
def add_student(roll, name, grade):
    if roll not in student_grades:
        student_grades[roll] = {"name": name, "grade": grade}
        print(f"Added Roll No: {roll}, Name: {name}, Grade: {grade}")
    else:
        print(f"Roll No {roll} already exists!")

# Update a student
def update_student(roll, name=None, grade=None):
    if roll in student_grades:
        if name:
            student_grades[roll]["name"] = name
        if grade is not None:
            student_grades[roll]["grade"] = grade
        print(f"Updated Roll No: {roll}, Name: {student_grades[roll]['name']}, Grade: {student_grades[roll]['grade']}")
    else:
        print(f"Roll No {roll} not found!")

# Delete a student
def delete_student(roll):
    if roll in student_grades:
        del student_grades[roll]
        print(f"Roll No {roll} has been successfully deleted")
    else:
        print(f"Roll No {roll} not found!")

# View all students
def display_all_student():
    if student_grades:
        print("\n--- Student Records ---")
        for roll, info in student_grades.items():
            print(f"Roll No: {roll}, Name: {info['name']}, Grade: {info['grade']}")
    else:
        print("No students found/added")

# Main function
def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View all students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            roll = input("Enter roll number = ")
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter student grade = "))
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            add_student(roll, name, grade)

        elif choice == 2:
            roll = input("Enter roll number = ")
            name = input("Enter new name (leave blank to keep same) = ")
            grade_input = input("Enter new grade (leave blank to keep same) = ")
            grade = int(grade_input) if grade_input else None
            update_student(roll, name if name else None, grade)

        elif choice == 3:
            roll = input("Enter roll number = ")
            delete_student(roll)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
