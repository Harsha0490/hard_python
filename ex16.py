from sys import argv

# setting the script and an argument 'filename' to argv
script, filename = argv


# printing that we are going to erase whatever param is passed into filename
print "We're going to erase %r." % filename
# printing "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit CTRL-C (^C)."
# printing "If you do want that, hit RETURN."
print "If you do want that, hit RETURN."

# prompting for user input with '?'
raw_input("?")

# print opening the file
print "Opening the file..."
# setting variable 'target' to built-in function open() with arg 'filename' and 'w' passed in
target = open(filename, 'w')

# print "Truncating the file. Goodbye!"
print "Truncating the file. Goodbye!"
# variable 'target' being truncated
target.truncate()

# printing "Now I'm going to ask you for three lines."
print "Now I'm going to ask you for three lines."

# setting line1-3 variables to raw_input with corresponding prompts for input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# printing "I'm going to write these to the file."
print "I'm going to write these to the file."

# writing the user's input for each line variable to the file set to 'target' variable.
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

writeLine = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write (writeLine)

# printing to let the user know the file is about to be closed.
print "And finally, we close it."
target.close()

# List of Commands to Remember
# close - Closes the file. Like 'File->Save..' in your editor.
# read - Reads the contents of the file. You can assign the result to a variable.
# readline - Reads just one line of a text file. 
# truncate - Empties the file. Watch out if you care about the file. 
# write('stuff') - Writes 'stuff' to the file.

# write takes a parameter of a string you want to write to the file. 

# 2. Write a script similar to the last exercise that uses 'read' and 'argv'
# to read the file you just created.

# 3. 
# writeLine = "%s\n%s\n%s\n" % (line1, line2, line3)
# target.write (writeLine)

# 4. Why we had to pass a 'w' as an extra parameter to 'open':
# it's justa string with a character in it for the kind of mode for the file.
# if you use 'w' then you're saying "open this file in 'write' mode", 
# thus the 'w' character.  There's also 'r' for "read," 'a' for append, 
# and modifiers on these. Makes the function explicit to enforce the opportunity
# for the file to be overwritten when the script is run. 

# 5. No. This question to teach us to read the documentation and also to understand every part of code you
# copy and paste from somewhere before you copy-paste it. It is actually very redundant.  
# if you have the write mode turned on then you don't need to truncate the target as well
# since 'w' instructs the runner to do so. 