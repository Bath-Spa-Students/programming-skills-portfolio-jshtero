# Making the list of sandwiches and the empty list.
sandwich_orders = ['beef', 'roast chicken', 'ham', 'tuna', 'pastrami']
finished_sandwiches = []

# This statement checks if pastrami is in the sandwich_orders and prints the statement while removing the option pastrami.
print("We are currently out of pastrami this evening.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# This statement uses pop to print each value stored in sandwich_orders in a message then uses append to append the sandwiches to the empty list.
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("I am currently making your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

# This statement uses the for loop to print the finished_sandwhiches.
for sandwich in finished_sandwiches:
    print("I have finished making your " + sandwich + " sandwich.")

