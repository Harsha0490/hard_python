print "Let's practice everything."
# \' escape necessary for apostrophe
# \\ prints a single forward slash
# \n starts a new line
print "You\'d need to know \'bout escapes with \\ that do \nnewlines and tabs."

# triple quotes produces a text block
# \t produces a tab
# \n starts a new line
# \n\t\t new line with a double tab
# this text block is the value given to the variable 'poem'
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# printing poem between two printed strings of 14 underscores
print "______________"
print poem
print "______________"


# variable 'five' is equal to 5. following line prints the value of variable 'five'
# in place of '%s' in the given string.
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# function "secret_formula" is being passed the variable 'started'
# jelly_beans multiplys whatever value 'started' is given by 500
# jars divides the value of the variable jelly_beans by 1000
# crates divides the value of jars by 100
# and finally, the function then returns the value
# for each of the three variables
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# sets variable start_point to 10000
start_point = 10000
# sets three variables to function 'secret_formula' with
# value of variable 'start_point' (10000) passed in.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)