from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Resultado: {randint(1, self.sides)}")

first_die = Die()

print("First die:")
for roll_number in range(10):
    first_die.roll_die()


print()

second_die = Die(10)

print("Second die:")
for roll_number in range(10):
    second_die.roll_die()

print()

third_die = Die(20)

print("Third die:")
for roll_number in range(10):
    third_die.roll_die()
