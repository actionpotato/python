##################
# set variables #
#################

# Set value of cars
cars = 100

# Define space in a cars
space_in_a_car = 4.0

# set number of drivers
drivers = 30

# Set number of passengers
passengers = 90

# calcualte cars minus drivers, and set it to a variable called cars_not_driven
cars_not_driven = cars - drivers

# set varible cars_driven to the drivers variable (30 originally)
cars_driven = drivers

# set carpool capacity, and calculate it
carpool_capacity = cars_driven * space_in_a_car

# calculate average_passengers_per_car from variables
average_passengers_per_car = passengers / cars_driven

#######################
# Start printing here #
#######################

# print number of cars available in sentence
print "There are", cars, "cars available."

# print number of drivers in a sentence
print "there are only", drivers, "drivers available."

# print empty cars
print "There will be", cars_not_driven, "empty cars today."

# print number of people we could move in a carpool
print "We can transport", carpool_capacity, "people today."

# print passengers
print "We have", passengers, "to carpool today."

# printe average passengers per car
print "We need to put about", average_passengers_per_car, "in each car."
