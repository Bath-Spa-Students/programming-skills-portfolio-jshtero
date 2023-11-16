# Creates variable personsage with the string to ask the user for his/hers age
personsage = "What is your age?"
print(personsage)
# Uses int(input) to receive the persons age and uses if, elif, else chain to print messages according the received input using comparison operators
age = int(input("Enter your age: "))
if (age) < 3:
    print ("Your movie ticket is free.")
elif (age) < 12:
    print ("Your movie ticket costs 10$")
else:
    (age) > 12
    print ("Your movie ticket costs 15$")



