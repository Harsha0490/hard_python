age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
	
	
# Rachels-iMac:hard_python rachelshatkin$ pydoc raw_input
# 
# Help on built-in function raw_input in module __builtin__:
# 
# raw_input(...)
#     raw_input([prompt]) -> string
#     
#     Read a string from standard input.  The trailing newline is stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.
# (END) 


# Rachels-iMac:hard_python rachelshatkin$ pydoc open
# 
# Help on built-in function open in module __builtin__:
# 
# open(...)
#     open(name[, mode[, buffering]]) -> file object
#     
#     Open a file using the file() type, returns a file object.  This is the
#     preferred way to open a file.  See file.__doc__ for further information.
# (END) 

# pydoc file
# Open a file. The mode can be 'r', 'w' or 'a' for reading (default), 
# writing or appending. The file will be created if it doesn't exist when opened
# for writing.  Add a 'b' to the mode for binary files. 
# Add a '+' to the mode to allow simultaneous reading and writing. 
# If the buffering argument is given, 0 means unbuffered, 1 means line
# buffered, and larger numbers specify the buffer size.
# The preferred way to open a file is with the builtin open() funciton
# Add a 'U' to mode to open the file for input with universal newline support.
# Any line ending in the input file will be seen as a '\n' in Python.
# Also, a file so opened gains the attribute 'newlines';
the value for this attribute is one of None (no newline read yet),
# '\r', '\n', '\r\n' or a tuple containing all the newline types seen.
# 'U' cannot be combined with 'w' or '+' mode.

# pydoc os
# os - OS routines for Mac, NT, or Posix depending on what system we're on.

# pydoc sys
# This module provides access to some objects used or maintained by the 
# interpreter and to functions that interact strongly with the interpreter.





# pydoc command
# pydoc is the documentation generation system for Python.
#
# module that automatically generates documentation from Python modules. 
# The documentation can be presented as pages of text on the console, 
# served to a web broswer, or saved to HTML files. 

# for modules, classes, functions and methods, the displayed 
# documentation is derived from the docstring (i.e. the '_doc_' attribute)
# of the object, and recursively of its documentable members.
# If there is no docstring, pydoc tries to obtain a description from the 
# block of comment lines just above the definition of the class, function
# or method in the source file, or at the top of the module. >>> (inspect.getcomments())

