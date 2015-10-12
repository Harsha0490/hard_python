# this is called an "import" - how you add features to your script from Python feature set.
# you tell python what you plan to use here. 
# keeps programs small, but also acts as documentation for other programmers.

from sys import argv

# this line "unpacks" argv so that, rather than holding all the arguments, 
# it gets assigned to four variables you can work with: script, first, second, and third.

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", raw_input()



# argv is the "argument variable" a very standard name in programming, used in 
# many languages. It 'holds' the arguments you pass to your Python script when you run it.
# 
# "features" aka "modules" - the things you 'import' to make the python program do more.
# may also be called "libraries"

# if i get an error it is telling me that i do not have enough arguments to unpack 
# in order for script to run. It will state how many i need.
# 
# if i give too many arguments it will also error out and tell me "too many values to unpack"
# 
# MODULES GIVE YOU FEATURES! 