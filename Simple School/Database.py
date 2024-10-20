import mysql.connector

class Database:
    def __init__(self):
        # Connect to the MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school_db"
        )
        self.cursor = self.conn.cursor()

    # Student operations
    def add_student(self, student):
        sql = "INSERT INTO students (student_id, firstname, surname, age, nationality, email, phone_num) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (student.student_id, student.firstname, student.surname, student.age, student.nationality, student.email, student.phone_num)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Student added successfully!")

    def remove_student(self, student_id):
        sql = "DELETE FROM students WHERE student_id = %s"
        values = (student_id,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Student removed successfully!")

    def get_students(self):
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # Teacher operations
    def add_teacher(self, teacher):
        sql = "INSERT INTO teachers (teacher_id, firstname, surname, subject) VALUES (%s, %s, %s, %s)"
        values = (teacher.teacher_id, teacher.firstname, teacher.surname, teacher.subject)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Teacher added successfully!")

    def remove_teacher(self, teacher_id):
        sql = "DELETE FROM teachers WHERE teacher_id = %s"
        values = (teacher_id,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Teacher removed successfully!")

    def get_teachers(self):
        sql = "SELECT * FROM teachers"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # Administration operations
    def add_administration(self, admin):
        sql = "INSERT INTO administration (admin_id, name, position) VALUES (%s, %s, %s)"
        values = (admin.admin_id, admin.name, admin.position)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Administration staff added successfully!")

    def remove_administration(self, admin_id):
        sql = "DELETE FROM administration WHERE admin_id = %s"
        values = (admin_id,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Administration staff removed successfully!")

    def get_administration(self):
        sql = "SELECT * FROM administration"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
