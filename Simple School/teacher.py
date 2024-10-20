class Teacher:
    def __init__(self, teacher_id, firstname, surname, subject):
        self.teacher_id = teacher_id
        self.firstname = firstname
        self.surname = surname
        self.subject = subject

    def __str__(self):
        return f"ID: {self.teacher_id}, Name: {self.firstname} {self.surname}, Subject: {self.subject}"
