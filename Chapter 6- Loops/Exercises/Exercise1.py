# Creates a variable using \t to add a space
pizzatopping = "\tWhat kind of topping would you like on your pizza?"
# Adds another variable to an already existing variable using +
pizzatopping += "\tSay 'Quit' once you have finished adding the toppings you like: "
# Uses the while true function and concatenation of strings to receive input until given the input Quit to break and end the code
while True:
    topping = input(pizzatopping)
    if topping != 'Quit':
        print(" Sure I'll add " + topping + " to the pizza you have ordered.")
    else:
        break