# Creates a variable called age to receive integer input from the user
age = int(input("Enter your age: "))
# Uses comparison operators to print different messages depending on the input from the user
if int(age) < 2:
    print ("You are a baby.")
elif int(age) < 4:
    print ("You are a toddler.")
elif int(age) < 13:
    print ("You are a kid.")
elif int(age) < 20:
    print ("You are a teenager.")
elif int(age) < 65:
    print ("You are an adult.")
else:
    int(age) > 65
    print ("You are an elder.")