# Stores the names of dead people in a list in the variable called "deadpeople"
deadpeople = ["Elvis Presley", "Michael Jackson", "Kobe Bryant"]
# Uses for loop to send a message to each dead person using concatenation
for peoplewhoaredead in deadpeople:
    print("I would like formally invite you, " + peoplewhoaredead + " to an extravagant dinner.")
# Changes one of the values in the list and prints a message saying one of the people who couldn't make it
deadpeople = ["Marilyn Monroe", "Michael Jackson", "Kobe Bryant"]
for peoplewhoaredead in deadpeople:
    print("Sadly one of the people I invited couldn't make it so I would like to formally invite you " + peoplewhoaredead + " to dinner.")