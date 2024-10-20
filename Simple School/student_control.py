from student import Student
from Database import Database

class StudentControl:
    def __init__(self):
        self.db = Database()

    def manage_students(self):
        while True:
            print("\nStudent Management Menu:")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View All Students")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                self.view_students()
            elif choice == '4':
                print("Exiting Student Management...")
                break
            else:
                print("Invalid choice, please try again.")

    def add_student(self):
        # Get student details from user
        student_id = int(input("Enter student ID: "))
        firstname = input("Enter student's first name: ")
        surname = input("Enter student's surname: ")
        age = int(input("Enter student's age: "))
        nationality = input("Enter student's nationality: ")
        email = input("Enter student's email: ")
        phone_num = input("Enter student's phone number: ")

        # Create a student object (if needed)
        student = Student(student_id, firstname, surname, age, nationality, email, phone_num)

        # Add student to the database
        self.db.add_student(student)

    def remove_student(self):
        # Get student ID to remove
        student_id = int(input("Enter student ID to remove: "))
        self.db.remove_student(student_id)

    def view_students(self):
        # Fetch and display all students from the database
        students = self.db.get_students()
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]} {student[2]}, Age: {student[3]}, Nationality: {student[4]}, Email: {student[5]}, Phone: {student[6]}")
