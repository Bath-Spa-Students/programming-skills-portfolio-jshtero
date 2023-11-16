# In this statement  I use def to define my function using variables size and message and adding default values to them.
def make_shirt(size = 'Large', message = 'I love Python'):
    print (" I'm going to make a " + size + " t-shirt.")
    print (" On the front of the shirt it will say " + message + ".")

# In this statement the first line prints the default output and in the second the value of size is changed and on the third both values are changed.
make_shirt()
make_shirt(size = 'Medium')
make_shirt('Extra Large', 'I like HTML' )
