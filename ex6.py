# set variable x equal to a string with a format character
x = "There are %d types of people." % 10
# set variable binary equal to string "binary"
binary = "binary"
# set variable do_not equal to "don't"
do_not = "don't"
# set variable y to string with two formatting characters,
# each of which are a previously defined variable
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x
print x
# print variable y
print y

# print string with formatting character pointed to variable x
print "I said: %r." % x
# print string with formatting character point ed to variable y
print "I also said: '%s'." % y

# set variable hilarious equal to False
hilarious = False
# set variable joke_evaluation equal to string with a formatting character
joke_evaluation = "isn't that joke so funny?! %r"

# print two variables concatenated
print joke_evaluation % hilarious

# set variable w to string
w = "This is the left side of..."
# set variable e to string
e = "a string with a right side."

# print variables w and e concatenated
print w + e


# 2/3. 5
# 4. concatenating two strings together makes one long string

# difference between %r and %s:
# Use the %r for debugging, since it displays the "raw" data of the variable,
# but the others are used for displaying to users.

# What's the point of %s and %d when you can just use %r?
# The %r is best for debugging, and the other formats are
# for actually displaying variables to users.