# Stores keys and values of great rivers and the countries they currently are in
dictionary = {"Yellow River": "China",
    "Colorado River": "United States",
    "Ganges River": "India",}
# Uses for loop to neatly present the great rivers and countries stored in the dictionary
for greatriver, Country in dictionary.items():
    print ("The " + greatriver.title() + " runs through " + Country.title() + ".")
print ("\tThese are three of the greatest rivers: ")
for greatriver in dictionary.keys():
    print ("| " + greatriver.title())
print ("\tThese are the countries they belong to: ")
for Country in dictionary.values():
    print ("| " + Country.title())