# defining and creating a function 'cheese_and_crackers' and passing it two arguments 
# 'cheese_count' and 'boxes_of_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# the following get printed when the function is called with each designated argument included.
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# printing that we can give the function numbers directly by passing them 
# in as arguments following	the function call
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# printing that we can use variables from our script to fill in the arguments for the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# calling the function using the variables defined in script
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# printing that we can do math inside the arguments for the function as well.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# printing that we can combine variables AND math for the args.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def smores(graham_crackers, marshmallows, chocolate):
	print "You have %r graham crackers!" % graham_crackers
	print "You have %r marshmallows!" % marshmallows
	print "You have %r pieces of chocolate!" % chocolate
	print "Time for S'MORE!\n"
	
smores(20, 30, 35)

smores(20 * 3, 25 * 2, 30)

graham_cracker_count = 20
marshmallow_count = 30
chocolate_count = 40

smores(graham_cracker_count, marshmallow_count, chocolate_count)

smores(graham_cracker_count - 10, marshmallow_count - 5, chocolate_count - 20)

smores(graham_cracker_count * 2, marshmallow_count * 1, chocolate_count / 2)

smores(graham_cracker_count * marshmallow_count, marshmallow_count * 2, chocolate_count + 100)

smores(20 + 30, 40 + 10, 50)

smores(100, 200, 150)

smores(marshmallow_count, marshmallow_count, marshmallow_count)

print "How many graham crackers do you have?",
graham_cracker_count = raw_input()
print "How many marshmallows do you have?",
marshmallow_count = raw_input()
print "How many chocolate bars do you have?",
chocolate_count = raw_input()

smores(graham_cracker_count, marshmallow_count, chocolate_count)