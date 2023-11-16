# Creates a list containing types of sandwhiches 
sandwich_orders = ['beef', 'roast chicken', 'ham', 'tuna']
# Creates an empty list to store finished sandwhiches
finished_sandwiches = []
# Uses while function and concatenation then uses pop to select the sandwhich you picked and appends it to the finished sandwhiches list
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("I am currently making your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)
# Uses for loop function and concatenation to create messages for finished_sandwhiches
for sandwich in finished_sandwiches:
    print("I have finished making your " + sandwich + " sandwich.")

