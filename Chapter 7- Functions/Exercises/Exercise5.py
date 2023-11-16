# Defining my function using two arguments one with no default value and one with a default value.
def describe_city(nameofcity, country = 'Italy'):
# Here I use ".title()" on the first part it receives any value given to it and the second ".title()" prints the string assigned to the variable "country".
    countryandcity = nameofcity.title() + " is located in " + country.title()
    print (countryandcity)

#In this statement I define my value to the variable name of city and on the second line I change the value of country to "United Arab Emirates" for a different output.
describe_city('Florence')
describe_city('Dubai', 'United Arab Emirates')
describe_city('Rome')
