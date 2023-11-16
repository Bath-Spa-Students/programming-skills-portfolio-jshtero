# Uses def to create a user defined function
def area_of_circle(r):
    pi=3.147
    area = pi*r*r
    return area
# Uses float input to retrieve input from the users radius and calculates it to get the area of the circle then prints the Area using the defined function given earlier
radius=float(input("Enter Radius: "))
print("Area: ",area_of_circle(radius))