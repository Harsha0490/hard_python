ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() # pop(stuff) - call pop on stuff
print ' '.join(stuff) # join('', stuff) - call join on this ' ' string,
# and apply to list items in stuff.
print '#'.join(stuff[3:5]) # join('#', stuff(range(3,5)) - call join on '#' and apply to
# list items with the indexes of 3 and 5.

