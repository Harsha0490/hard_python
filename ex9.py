# Here's some new strange stuff, remember type it exactly

# defining variable days as equal to a string of days of the week
# when printed, all on same line as written between double quotes
days = "Mon Tue Wed Thu Fri Sat Sun"
# defining variable days as equal to a string of the months, 
# when printed this way, they are each on their own line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints a string followed by the days of the week on one line
print "Here are the days: ", days
# prints a string followed by months, each on it's own line after 'jan'
print "Here are the months: ", months

# prints a block of text. triple double quotes allow this.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""