# Uses argv to get a filename.  From the module named sys,
# import a the thing named 'argv' into the current name context.
# this makes it possible to refer to 'argv' without having to mention the module it came from. 

from sys import argv


# first argument to a command-line executable is the script name, 
# and the rest are the expected arguments
# argv is a list that is expected to contain 2 values: the script name
# ('script') and an argument ('filename')
# can also be written as:
# 	script = argv[0]
#	filename = argv[1]

script, filename = argv


# defining variable 'txt' as 'open(filename)'.
# prompting terminal to open a given file based on the file name passed into the 
# 'filename' argument. 

txt = open(filename)


# print "Here's your file %r:" and fill in %r for
# parameter passed into argument 'filename'
print "Here's your file %r:" % filename


# print the contents of the designated file via "read" command
print txt.read()


# print prompt "Type the filename again:" followed by a variable 'file_again' assigned
# as an input
print "Type the filename again:"
file_again = raw_input("> ")

# variable 'txt_again' being defined as command open input assigned to variable 'file_again'
txt_again = open(file_again)

# print contents of file/param assigned to variable 'txt_again'
print txt_again.read()

txt.close()
txt_again.close()


#argv is a list containing the arguments passed to the python 
# interpreter when called from a command line. 

# python open
# open ()
# open a file, returning an object of the 'file' type. 

# commands also called 'functions' and 'methods'
# e.g. 'open()' is a built-in function
# 

# 4. Get rid of the lines 10-15 where you use raw_input and run the script again.
# 5. Use only raw_input and try the script that way. Why is one way of getting 
# the filename would be better than another?
# the first is better because it is more automated. The latter requires you to input
# the file name yourself as opposed to just passing it in. Much less convenient.

# in python
#
# >>> open('ex15_sample.txt')
# 	<open file 'ex15_sample.txt', mode 'r' at 0x108b446f0>

# >>> open('ex15_sample.txt').read()
# 	'This is stuff I typed into a file.\nIt is really cool stuff.\nLots and lots of fun to have in here.'
# 

