#initialsing dictionary
student_grades = {  }

#add a new student
def add_student(name, grade):
    student_grades[name] = grade
    #yaha pe naam key hain aur marks grade hai
    print(f"Added {name} with a {grade}")
    #added [sagar] with a hundred

#update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #yaha pe jo key hain maanlo rashid aur uska updated marks jo hain wo 200 hain to wo upar ke rashid key me update ho jaayga 
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")

#Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")

#view all students
def display_all_student(  ):
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    
    else:
        print("No students found/added")

def main(  ):
    while True:
        print('\n student grade management system')
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit")

        choice = int(input("enter your choice = "))
        if choice == 1:
            name = input("enter student name = ")
            grade = int(input("enter student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("enter student name = ")
            grade = int(input("enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_student(  )

        elif choice == 5:
            print("closing the program....")
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main()