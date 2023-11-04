pizzatopping = "\tWhat kind of topping would you like on your pizza?"
pizzatopping += "\tSay 'Quit' once you have finished adding the toppings you like: "
while True:
    topping = input(pizzatopping)
    if topping != 'Quit':
        print(" Sure I'll add " + topping + " to the pizza you have ordered.")
    else:
        break