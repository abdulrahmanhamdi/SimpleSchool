from student_control import StudentControl
from teacher_control import TeacherControl
from administration_control import AdministrationControl

def main():
    print("Welcome to the School Management System")

    # Initialize control classes
    student_ctrl = StudentControl()
    teacher_ctrl = TeacherControl()
    admin_ctrl = AdministrationControl()

    while True:
        print("\nMenu:")
        print("1. Manage Students")
        print("2. Manage Teachers")
        print("3. Manage Administration")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Managing students
            student_ctrl.manage_students()
        elif choice == '2':
            # Managing teachers
            teacher_ctrl.manage_teachers()
        elif choice == '3':
            # Managing administration
            admin_ctrl.manage_administration()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
