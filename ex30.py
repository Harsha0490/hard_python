# Setting variables "people" "cars" and
# "trucks" to initial values
people = 15
cars = 20
trucks = 30

# if there are more cars than people, print the following:
if cars > people:
    print "We should take the cars."
# otherwise, if there are less cars than people, print this:
elif cars < people:
    print "We should not take the cars."
# if neither of the above are true, then just print this:
else:
    print "We can't decide."

# if there are more trucks than cars, print this:
if trucks > cars:
    print "That's too many trucks."
# otherwise, if there are less trucks than cars
# print this instead:
elif trucks < cars:
    print "Maybe we could take the trucks."
# if none of the above statements are true, print this:
else:
    print "We still can't decide."

# if there are less people than trucks,
# AND amount of trucks are equal to
# the amount of cars print this:
if people < trucks and trucks == cars:
    print "We have a good variety to choose from"

#if there are more people than trucks, print this:
if people > trucks:
    print "Alright, let's just take the trucks."
# otherwise, print this:
else:
    print "Fine, let's stay home then."