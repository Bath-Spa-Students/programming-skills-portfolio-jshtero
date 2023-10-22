deadpeople = ["Elvis Presley", "Michael Jackson", "Kobe Bryant", "Bruce Lee"]
for peoplewhoaredead in deadpeople:
    print("I would like formally invite you, " + peoplewhoaredead + " to an extravagant dinner.")
deadpeople = ["Marilyn Monroe", "Michael Jackson", "Kobe Bryant", "Bruce Lee"]
for peoplewhoaredead in deadpeople:
    print("Sadly one of the people I invited couldn't make it so I would like to formally invite you " + peoplewhoaredead + " to dinner.")
peoplewhoaredead = deadpeople.pop(2)
print (deadpeople)
peoplewhoaredead = deadpeople.pop(1)
print (deadpeople)
for peoplewhoaredead in deadpeople:
    print ("The two of you, " + peoplewhoaredead + " are still formally invited to dinner.")
print (deadpeople)
if len(deadpeople) >= 2:
    del deadpeople[-2:]
print (deadpeople)
