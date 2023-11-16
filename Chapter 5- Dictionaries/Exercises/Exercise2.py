# Creates a dictionary called glossary storing keys and values with definitions of the keys
glossary = {"Variable": "In programming a variable is a memory used to allocate and store a value whether it is a number word or letter.",
    "Input": "In programming input is used to receive input from the user such as age.",
    "Print": "In programming the function print is used to print out a statement and shows its output.",
    "Output": "In programming output is what is shown when printing the input of the program. Output displays the result.",
    "List": "List in python is used to store multiple values.",}
# In these statements we concatenate messages using the keys and using the values to print the message displaying the output values of the dictionary neatly.
word = "Variable"
print ("\n" + word.title() + ": " + glossary[word])

word = "Input"
print ("\n" + word.title() + ": " + glossary[word])

word = "Print"
print ("\n" + word.title() + ": " + glossary[word])

word = "Output"
print ("\n" + word.title() + ": " + glossary[word])

word = "List"
print ("\n" + word.title() + ": " + glossary[word])