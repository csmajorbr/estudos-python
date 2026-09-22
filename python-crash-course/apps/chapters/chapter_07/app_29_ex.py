sandwich_orders = ['pastrami', 'grilled cheese', 'pastrami',
                   'turkey sandwich', 'ham sandwich', 'grilled chicken sandwich', 'pastrami']

finished_sandwiches = []

print("The snack bar is out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"The {current_sandwich.title()} is ready.")

print("\n---SANDWICHES---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
