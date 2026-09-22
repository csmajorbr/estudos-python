sandwich_orders = ['grilled cheese', 'turkey sandwich', 'ham sandwich', 'grilled chicken sandwich']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"The {current_sandwich.title()} is ready.")

print("\n---- Sandwiches ----")
count = 1
for sandwich in finished_sandwiches:
    
    print(f"{count}º {sandwich.title()}.")
    count += 1
