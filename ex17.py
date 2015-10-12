from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# len() gets the length of the string that you pass to it then returns that as a number.
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists (to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# using import is a way to get tons of free code other programmers 
# have written so you do not have to write it. 

# 1/2. Try to make the script more friendly to use by removing features. 
# see how short you can make the script

# in_file = open(from_file, 'r')
# 
# out_file = open(to_file, 'w')
# 
# out_file.close()
# in_file.close()

# 3 *cat*
# concatenate and print files
# utility that reads files sequentially, writing them to the standard output.  
# The file operands are processed in command-line order.
# options:
# -b	Number the non-blank output lines, starting at 1.
# -e 	Display non-printing characters (see the -v option), and display a dollar sign ('$') 
# 	at the end of each line.
# -n	Number the output lines, starting at 1
# -s	Squeeze multiple adjacent empty lines, causing the output to be single spaced.
# -t	Display non-printing characters (see the -v option), and display tab characters as '^I'
# -u	Disable output buffering.
# -v	Display non-printing character so they are visible. 

# 4. why close out_file? 
# python does not promise that it will close the files for you.  
# The operating system does when the program exits. 
# If your program does something else for a while, 
# or repeats this sequence of steps dozens of times, 
# you could run out of resources, or overwrite something. SAFETY!

# 5. 'Import' statement
# executed in 2 steps:
# 1. find a module, and initialize it if necessary
# 2. define a name or names in the local namespace 
# (of the scope where the 'import' statement occurs)
# 
# The statement comes in two forms differing on whether it uses the 'from' keyword. 
# The first form (without 'from') repeats these steps for each identifier in the list.  
# The form with 'from' performs step 1 once, and then performs step 2 repeatedly.

