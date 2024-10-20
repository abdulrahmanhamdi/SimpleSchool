from teacher import Teacher
from Database import Database


class TeacherControl:
    def __init__(self):
        self.db = Database()

    def manage_teachers(self):
        while True:
            print("\nTeacher Management Menu:")
            print("1. Add Teacher")
            print("2. Remove Teacher")
            print("3. List Teachers")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_teacher()
            elif choice == '2':
                self.remove_teacher()
            elif choice == '3':
                self.list_teachers()
            elif choice == '4':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice, please try again.")

    def add_teacher(self):
        # Get teacher details from user
        teacher_id = input("Enter teacher ID: ")
        name = input("Enter teacher name: ")
        subject = input("Enter teacher subject: ")

        # Create a teacher object
        teacher = Teacher(teacher_id, name, subject)

        # Add the teacher to the database
        self.db.add_teacher(teacher)
        print("Teacher added successfully!")

    def remove_teacher(self):
        # Get teacher ID to remove
        teacher_id = input("Enter teacher ID to remove: ")
        self.db.remove_teacher(teacher_id)
        print(f"Teacher with ID {teacher_id} removed successfully!")

    def list_teachers(self):
        # Fetch all teachers from the database
        teachers = self.db.get_teachers()

        # If no teachers found
        if not teachers:
            print("No teachers found.")
        else:
            # List all teachers
            print("\nTeacher List:")
            for teacher in teachers:
                print(f"ID: {teacher[0]}, Name: {teacher[1]}, Subject: {teacher[2]}")
