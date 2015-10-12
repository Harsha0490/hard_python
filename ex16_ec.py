from sys import argv

script, filename = argv

print "Printing the file you just asked for...\n"
txt = open(filename)
print txt. read()

print "What file do you need?"
filename = raw_input("> ")

txt_again = open(filename)
print txt_again.read()