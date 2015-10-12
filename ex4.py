
# setting variable 'cars' to 100
cars = 100
# setting variable 'space in a car' to 4.0
space_in_a_car = 4.0
# setting variable 'drivers' to 30
drivers = 30
# setting variable 'passengers' to 90
passengers = 90
# setting variable 'cars_not_driven' to cars - drivers
cars_not_driven = cars - drivers
# setting variable 'cars_driven' to variable 'drivers'
cars_driven = drivers
# setting variable 'carpool_capacity' to cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# setting variable 'average_passengers_per_car' to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

# printing the number of cars available
print "There are", cars, "cars available."
# printing the number of drivers available
print "There are only", drivers, "drivers available."
# printing the number of cars that will not be driven
print "There will be", cars_not_driven, "empty cars today."
# printing the number of people that can be transported
print "We can transport", carpool_capacity, "people today."
# printing the number of passengers that need carpooling
print "We have", passengers, "to carpool today."
# printing how many passengers needed in each car
print "We need to put about", average_passengers_per_car, "in each car."


# STUDY DRILLS

# Explain the following error:
#
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
#
# Explanation: 'car_pool_capacity' is not a defined variable
# it should be written as 'carpool_capacity' (less one underscore)
#
# 1/2. Since there are no decimal answers in any of these equations, 
# the floating point number is not entirely necessary.
# should there be a need for an answer with a decimal, however,
# this would come in handy so rounding to the nearest whole number 
# doesn't occur. Floating point number = number with a decimal point
#
# 3. done
#
# 4. '=' is called 'equals'. assigns values to variables 
# (assigns names to values)
#
# 5. '_' is an underscore character


# FIBONACCI SEQUENCE (command line calculator) 
# >>> def fib(n): #write Fibonacci series up to n
# ...	"""Print a Fibonacci series up to n."""
# ...	a, b = 0, 1
# ...	while b < n:
# ...		print b,
# ...		a, b = b, a + b
# ...
# >>> # Now call the function we just defined:
# ...fib(2000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# Difference between = and ==
# = assigns the value on the right to a variable on the left
# == tests if two things have the same value. (Exercise 27)