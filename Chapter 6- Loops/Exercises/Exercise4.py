sandwich_orders = ['beef', 'roast chicken', 'ham', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("I am currently making your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

for sandwich in finished_sandwiches:
    print("I have finished making your " + sandwich + " sandwich.")

