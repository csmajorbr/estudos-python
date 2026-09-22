class User:
    def __init__(self, first_name, last_name, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Login: {self.login}")
        print(f"Password: {self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('Mario', 'Botelho', 'mariobotelho', 12345)
print(f"Login attempts antes: {user_1.login_attempts}")

print()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f"Login attempts depois: {user_1.login_attempts}")

print()

user_1.reset_login_attempts()

print(f"Login attempts depois do reset: {user_1.login_attempts}")