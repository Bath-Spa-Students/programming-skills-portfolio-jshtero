peoplespets = [{"Type of animal": "Cat",
                "Owner": "John"},
                {"Type of animal": "Dog",
                 "Owner": "Denzel"},
                 {"Type of animal": "Turtle",
                  "Owner": "Joshua",},
                  {"Type of animal": "Bird",
                   "Owner": "Alex",}]

for peoplespet in peoplespets:
    print("\nType of pet that my friend owns - " + peoplespet['Owner'].title() + ": ")
    for key, value in peoplespet.items():
        print("\t" + key + ": " + str(value))