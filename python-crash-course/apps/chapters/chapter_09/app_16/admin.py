from user import User

class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete user",
            "can ban user"
            ]

    def show_privileges(self):
        for count, privilege in enumerate(self.privileges, start=1):
            print(f"Privilege {count}: {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, login, password):
        super().__init__(first_name, last_name, login, password)
        self.privileges = Privileges()