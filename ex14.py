from sys import argv

script, user_name, color = argv
prompt = '>>>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "I already know your favorite color is %r." % color
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Remind me your favorite color?"
color = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You living %r. Not sure where that is.
And you have a %r computer. And your favorite color is %r. Nice.
""" % (likes, lives, computer, color)