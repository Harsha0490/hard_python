# defining variable formatter as a string of format characters %r
formatter = "%r %r %r %r"

# print variable formatter as the following numbers, each for every %r included in variable
print formatter % (1, 2, 3, 4)
# print variable formatter as 4 strings, one for each %r formatter
print formatter % ("one", "two", "three", "four")
# print variable formatter as 4 booleans: True or False
print formatter % (True, False, False, True)
# print variable formatter four times, '%r %r %r %r' four times.
print formatter % (formatter, formatter, formatter, formatter)
# print variable formatter as four strings in a row
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# when printed in terminal, there are double quotes around "But it didn't sing." 
# instead of single quotes like the other strings because of the apostrophe in "didn't"

# Travis, explain to me what it means by '%r' is for debugging specifically. 
# I'm not grasping this concept yet.