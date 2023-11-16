# Creates a dictionary named peoplespets to represent keys and values as the types of animal and the owners
peoplespets = [{"Type of animal": "Cat",
                "Owner": "John"},
                {"Type of animal": "Dog",
                 "Owner": "Denzel"},
                 {"Type of animal": "Turtle",
                  "Owner": "Joshua",},
                  {"Type of animal": "Bird",
                   "Owner": "Alex",}]
# Uses for loop to present what type of pet that I know that my friend owns neatly.
for peoplespet in peoplespets:
    print("\nType of pet that my friend owns - " + peoplespet['Owner'].title() + ": ")
    for key, value in peoplespet.items():
        print("\t" + key + ": " + str(value))