# this one is like your scripts with argv:
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Describing "print_two" function
# 1. we tell python we want to make a function using 'def' for "define"
# 2. On the same line as 'def' we give the function a name 'print_two'
# 3. then we tell it we want *args (asterisk args) which is like 'argv'
# parameter but for functions.  This HAS to go inside the '()' to work.
# 4. Then end line with a ':', and start indenting
# 5. After ':' all lines are indented 4 spaces will become attached to 
# the name 'print_two'. First indented line is one that unpacks the arguments
# the same as with your scripts.
# 6. To demonstrate how it works we print these arguments out, 
# just like in a script.

# Functions:
# 1. Name pieces of code the way variables name strings and numbers.
# 2. They take arguments the way your scripts take 'argv'
# 3. Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands"

# Can create a function by using the word 'def' in Python. 

# COMMANDS ARE JUST FUNCTIONS! (open, exists, etc...)

# STUDY DRILLS - FUNCTION CHECKLIST
# 1. Did you start your function definition with 'def'?
# 2. Does your function name have only characters and '_' characters?
# 3. Did you put an open parenthesis right after the function name?
# 4. Did you put your arguments after the open parenthesis separated by commas?
# 5. Did you make each argument unique (meaning no duplicated names)?
# 6. Did you put a close parenthesis and a colon after the arguments?
# 7. Did you indent all lines of code you want in the function four spaces? 
# No more, no less.
# 8. Did you "end" your function by going back to writing with no indent
# (called 'dedenting')?

# When you run (i.e. "use" or "call" a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the opening parenthesis after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a closing parenthesis?

# Use these two checklists on the remaining lessons until you do not need them anymore. 

# "To 'run,' 'call,' or 'use' a function all mean the same thing."