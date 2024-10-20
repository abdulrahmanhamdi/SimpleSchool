class Administration:
    def __init__(self, admin_id, name, position):
        self.admin_id = admin_id
        self.name = name
        self.position = position

    def __str__(self):
        return f"ID: {self.admin_id}, Name: {self.name}, Position: {self.position}"
