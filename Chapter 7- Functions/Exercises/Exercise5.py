#In this statement I def to define my function and add two arguments one with the variable nameofcity and one variable called country with the default value "Italy".
def describe_city(nameofcity, country = 'Italy'):
    countryandcity = nameofcity.title() + " is located in " + country.title()
    print (countryandcity)

#In this statement I define my value to the variable name of city and on the second line I change the value of country to "United Arab Emirates" for a different output.
describe_city('Florence')
describe_city('Dubai', 'United Arab Emirates')
describe_city('Rome')
