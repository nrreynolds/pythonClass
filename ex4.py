cars = 2444
number_of_cars = 250
space_cars = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_cars
average_passengers_per_car = passengers / cars_driven

print('there are', cars, 'cars available.')
print('there are only', drivers, "drivers available")
print('there will be', cars_not_driven, "empty today")
print('we can transport', carpool_capacity, 'people today')
print('we have', passengers, 'to carpool today')
print('we need to put about', average_passengers_per_car, 'in each car')

# try some more using single letter variable names

i = "imagination"
x = "example"
z = 200

print("my", i, "is an", x, "of being", z, "years old")

#####  
