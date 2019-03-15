# Initialize variables
weight = 0.2
animal = "newt"

# Use these objects to print a sentence without '.format()' string method
print(weight, "kg is the weight of the", animal)

# Print the same line using empty {} place-holders
print("{} kg is the weight of the {}".format(weight, animal))

# Print the same line using indexed {} place-holders
print("{1} kg is the weight of the {0}".format(animal, weight))

# Print the same line by creating new string and float objects inside .format()
print("{weight1} kg is the weight of the {animal1}".format(weight1 = 0.2,
                                                           animal1 = "newt"))

# Print line again by creating formatted string literal using variables directly
print(f"{weight} kg is the weight of the {animal}")
                                                               
