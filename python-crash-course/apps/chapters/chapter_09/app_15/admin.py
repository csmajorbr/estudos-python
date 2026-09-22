class User:
    def __init__(self, first_name, last_name, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Login: {self.login}")
        print(f"Password: {self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

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