from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

my_ticket = [1, 5, 'a', 'e']

count = 0
while len(winning_ticket) < 4 and winning_ticket != my_ticket:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f" We pulled a {pulled_item}")
        winning_ticket.append(pulled_item)

    count += 1

print(f"\nThe final winning ticket is: {winning_ticket}")
print(count)
