# saying "from" the module "sys" import "argv" for the current program
# so we can refer to "argv" in our program.
from sys import argv

# telling python how we will be providing argument in command prompt
# i.e. "python script.py and the input file name or in this case, 'text.txt'"
script, input_file = argv

# defining and creating function 'print_all' and passing it an argument of 'f'
# then printing f (the variable) which represents the file we want to print. 
# .read() method reads bytes from file until EOF.
def print_all(f):
    print f.read()

# defining and creating function "rewind" and passing it an argument of 'f'
# seek method with default whence argument of '0' (absolute file positioning). 
# Setting the file's current position at offset in file 'f' 
def rewind(f):
    f.seek(0)

# defining and creating function "print_a_line", passing it arguments of 'line_count'
# and 'f'. Printing line_count and the readline of file 'f'
def print_a_line(line_count, f):
    print line_count, f.readline()

# setting variable 'current_file' to method 'open' passing it an argument of (input_file)
current_file = open(input_file)

# printing "First let's print the whole file:\n" with an end of line
print "First let's print the whole file:\n"

# method 'print_all' passing it variable 'current_file' which is
# opening the designated 'input_file' and printing its contents
print_all(current_file)

# printing "Now let's rewind, kind of like a tape."
print "Now let's rewind, kind of like a tape."

# method rewind on current_file. sets the file position indicator 
# (whence) to beginning of the file (or indicated whence argument).
rewind(current_file)

# printing "Let's print three lines:"
print "Let's print three lines:"

# setting var 'current_line' to '1'
current_line = 1

# function 'print_a_line' being passed arguments 'current_line' and 'current_file'
# printing out the current line within the current file
print_a_line(current_line, current_file)

# setting variable 'current_line' to equal 'current_line' + 1 line
# printing the current line in the current file (i.e. printing the next line)
current_line += 1
print_a_line(current_line, current_file)

# setting variable 'current_line' to equal 'current_line' + 1 line
# printing the current line in the current file (i.e. printing the next, next line)
current_line += 1
print_a_line(current_line, current_file)


# .read() method reads the file. 
# method returns the bytes read in string

# .seek() method sets the file's current position at the offset. 
# There is no return value. 
# offset = the position of the read/write pointer within the file
# whence = optional argument which defaults to 0 which means
# absolute file positioning, other values are 1 which means seek relative
# to the current position and 2 means seek relative to the file's end. 

# .readline() method reads one entire line from the file. 
# a trailing newline character is kept in the string. 
# if the size argument is present and non-negative, it is a maximum 
# byte count including the trailing newline and an incomplete line may be returned. 
# size = the number of bytes to be read from a file.