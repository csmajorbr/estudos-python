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

user_1 = User('Maria', 'Silva', 'Ma', '54321')
user_2 = User('Marcos', 'Ramos', 'Marquinhos', '12345')

user_1.describe_user()
user_1.greet_user()

print()

user_2.describe_user()
user_2.greet_user()
