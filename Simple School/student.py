class Student:
    def __init__(self, student_id, firstname, surname, age, nationality, email, phone_num):
        self.student_id = student_id
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.email = email
        self.phone_num = phone_num

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.firstname} {self.surname}, "
                f"Age: {self.age}, Nationality: {self.nationality}, Email: {self.email}, "
                f"Phone: {self.phone_num}")
