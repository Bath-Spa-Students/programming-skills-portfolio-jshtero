# Stores the names of dead people in a list in the variable called "deadpeople"
deadpeople = ["Elvis Presley", "Michael Jackson", "Kobe Bryant", "Bruce Lee"]
# Uses for loop to print a message to each dead person in the list
for peoplewhoaredead in deadpeople:
    print("I would like formally invite you, " + peoplewhoaredead + " to an extravagant dinner.")
# Changes the value of one of the dead people in the list and prints a message saying they could not make it
deadpeople = ["Marilyn Monroe", "Michael Jackson", "Kobe Bryant", "Bruce Lee"]
for peoplewhoaredead in deadpeople:
    print("Sadly one of the people I invited couldn't make it so I would like to formally invite you " + peoplewhoaredead + " to dinner.")
# Uses pop function to remove 2 dead people within the list
peoplewhoaredead = deadpeople.pop(2)
print (deadpeople)
peoplewhoaredead = deadpeople.pop(1)
print (deadpeople)
# Uses the if statement to look if there are 2 greater or equals to 2 then deletes the 2 remaining people within the list leaving the list empty
for peoplewhoaredead in deadpeople:
    print ("The two of you, " + peoplewhoaredead + " are still formally invited to dinner.")
print (deadpeople)
if len(deadpeople) >= 2:
    del deadpeople[-2:]
print (deadpeople)
