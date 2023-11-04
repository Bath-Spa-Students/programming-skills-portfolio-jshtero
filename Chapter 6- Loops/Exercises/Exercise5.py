sandwich_orders = ['beef', 'roast chicken', 'ham', 'tuna', 'pastrami']
finished_sandwiches = []

print("We are currently out of pastrami this evening.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("I am currently making your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

for sandwich in finished_sandwiches:
    print("I have finished making your " + sandwich + " sandwich.")

