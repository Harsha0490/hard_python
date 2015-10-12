# Print the following strings one at a time
print "Mary had a little lamb."
# print string with a string inserted via format character %s
print "Its fleece was white as %s." % 'snow'
# print string
print "And everywhere that Mary went."
# print string '.' multiply it by 10, gives 10 '.'s
print "." * 10 # what'd that do?

# defining variables end1 through end12
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens

# concatenating each variable together to form one string/ word "Cheese Burger"
# comma separates variables end1 - end6 from end7 - end12
# when i remove the comma it prints each print statement on its own line:
# Cheese
# Burger

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12