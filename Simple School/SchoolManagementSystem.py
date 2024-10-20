import tkinter as tk
from tkinter import ttk, messagebox

from Administration import Administration
from student import Student
from student_control import StudentControl
from teacher import Teacher
from teacher_control import TeacherControl
from administration_control import AdministrationControl


class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("600x400")

        # Initialize control classes
        self.student_ctrl = StudentControl()
        self.teacher_ctrl = TeacherControl()
        self.admin_ctrl = AdministrationControl()

        # Create tabs
        tab_control = ttk.Notebook(root)
        self.student_tab = ttk.Frame(tab_control)
        self.teacher_tab = ttk.Frame(tab_control)
        self.admin_tab = ttk.Frame(tab_control)

        tab_control.add(self.student_tab, text="Manage Students")
        tab_control.add(self.teacher_tab, text="Manage Teachers")
        tab_control.add(self.admin_tab, text="Manage Administration")
        tab_control.pack(expand=1, fill="both")

        self.create_student_tab()
        self.create_teacher_tab()
        self.create_admin_tab()

    def create_student_tab(self):
        tk.Label(self.student_tab, text="Add Student", font=("Arial", 14)).pack(pady=10)

        # Create input fields for Student
        tk.Label(self.student_tab, text="Student ID:").pack()
        self.student_id_entry = tk.Entry(self.student_tab)
        self.student_id_entry.pack()

        tk.Label(self.student_tab, text="First Name:").pack()
        self.student_firstname_entry = tk.Entry(self.student_tab)
        self.student_firstname_entry.pack()

        tk.Label(self.student_tab, text="Surname:").pack()
        self.student_surname_entry = tk.Entry(self.student_tab)
        self.student_surname_entry.pack()

        tk.Label(self.student_tab, text="Age:").pack()
        self.student_age_entry = tk.Entry(self.student_tab)
        self.student_age_entry.pack()

        tk.Label(self.student_tab, text="Nationality:").pack()
        self.student_nationality_entry = tk.Entry(self.student_tab)
        self.student_nationality_entry.pack()

        tk.Label(self.student_tab, text="Email:").pack()
        self.student_email_entry = tk.Entry(self.student_tab)
        self.student_email_entry.pack()

        tk.Label(self.student_tab, text="Phone Number:").pack()
        self.student_phone_entry = tk.Entry(self.student_tab)
        self.student_phone_entry.pack()

        # Submit button
        tk.Button(self.student_tab, text="Add Student", command=self.add_student).pack(pady=10)

    def create_teacher_tab(self):
        tk.Label(self.teacher_tab, text="Add Teacher", font=("Arial", 14)).pack(pady=10)

        # Create input fields for Teacher
        tk.Label(self.teacher_tab, text="Teacher ID:").pack()
        self.teacher_id_entry = tk.Entry(self.teacher_tab)
        self.teacher_id_entry.pack()

        tk.Label(self.teacher_tab, text="First Name:").pack()
        self.teacher_firstname_entry = tk.Entry(self.teacher_tab)
        self.teacher_firstname_entry.pack()

        tk.Label(self.teacher_tab, text="Surname:").pack()
        self.teacher_surname_entry = tk.Entry(self.teacher_tab)
        self.teacher_surname_entry.pack()

        tk.Label(self.teacher_tab, text="Subject:").pack()
        self.teacher_subject_entry = tk.Entry(self.teacher_tab)
        self.teacher_subject_entry.pack()

        # Submit button
        tk.Button(self.teacher_tab, text="Add Teacher", command=self.add_teacher).pack(pady=10)

    def create_admin_tab(self):
        tk.Label(self.admin_tab, text="Add Administration Staff", font=("Arial", 14)).pack(pady=10)

        # Create input fields for Administration
        tk.Label(self.admin_tab, text="Admin ID:").pack()
        self.admin_id_entry = tk.Entry(self.admin_tab)
        self.admin_id_entry.pack()

        tk.Label(self.admin_tab, text="Name:").pack()
        self.admin_name_entry = tk.Entry(self.admin_tab)
        self.admin_name_entry.pack()

        tk.Label(self.admin_tab, text="Position:").pack()
        self.admin_position_entry = tk.Entry(self.admin_tab)
        self.admin_position_entry.pack()

        # Submit button
        tk.Button(self.admin_tab, text="Add Admin Staff", command=self.add_administration).pack(pady=10)

    # Backend integration for adding students
    def add_student(self):
        student_id = self.student_id_entry.get()
        firstname = self.student_firstname_entry.get()
        surname = self.student_surname_entry.get()
        age = self.student_age_entry.get()
        nationality = self.student_nationality_entry.get()
        email = self.student_email_entry.get()
        phone_num = self.student_phone_entry.get()

        # You can add validation here before passing it to the backend
        try:
            student = Student(student_id, firstname, surname, int(age), nationality, email, phone_num)
            self.student_ctrl.db.add_student(student)
            messagebox.showinfo("Success", "Student added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Backend integration for adding teachers
    def add_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        firstname = self.teacher_firstname_entry.get()
        surname = self.teacher_surname_entry.get()
        subject = self.teacher_subject_entry.get()

        try:
            teacher = Teacher(teacher_id, firstname, surname, subject)
            self.teacher_ctrl.db.add_teacher(teacher)
            messagebox.showinfo("Success", "Teacher added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Backend integration for adding administration staff
    def add_administration(self):
        admin_id = self.admin_id_entry.get()
        name = self.admin_name_entry.get()
        position = self.admin_position_entry.get()

        try:
            admin = Administration(admin_id, name, position)
            self.admin_ctrl.db.add_administration(admin)
            messagebox.showinfo("Success", "Admin staff added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()
