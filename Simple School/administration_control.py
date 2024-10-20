from Administration import Administration
from Database import Database


class AdministrationControl:
    def __init__(self):
        self.db = Database()

    def manage_administration(self):
        while True:
            print("\nAdministration Management:")
            print("1. Add Administration Staff")
            print("2. Remove Administration Staff")
            print("3. List Administration Staff")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_administration()
            elif choice == '2':
                self.remove_administration()
            elif choice == '3':
                self.list_administration()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

    def add_administration(self):
        admin_id = input("Enter admin ID: ")
        name = input("Enter admin name: ")
        position = input("Enter admin position: ")
        admin = Administration(admin_id, name, position)
        self.db.add_administration(admin)

    def remove_administration(self):
        admin_id = input("Enter admin ID to remove: ")
        self.db.remove_administration(admin_id)

    def list_administration(self):
        administration_staff = self.db.get_administration()
        if administration_staff:
            for admin in administration_staff:
                print(admin)
        else:
            print("No administration staff found.")
