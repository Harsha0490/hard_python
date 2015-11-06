# Keyword Practice

# and - logical and. EX: True and False == False
# used if all conditions in a boolean expression must be met,
# otherwise false.


# as - part of the "with-as" statement. EX: with X as Y: pass
# used if we want to give a module a different alias.
# EX2: import random as rnd
#      for i in range(10):
#            print rnd.randint(1,10)
#
# importing random module. random given alias "rnd"


# assert - Assert (ensure) that something is true.
# EX: assert False, "Error!"
# used for debugging purposes.
# Can be used for testing conditions that are
# obvious to us.
# EX2: We know salary cannot be < 0
# so we can assert this in the code.
# if assertion fails, interpreter will complain.
#   salary = 3500
#   salary -= 3560 # a mistake was made here
#   assert salary > 0
#
# Execution of script will fail with an "AssertionError"


# break - stop this loop right now.
# EX: while True: break
# prevents infinite while loops/ program crashing
# used to interrupt cycle if needed.


# class - define a class
# EX: class Person(object)
# MOST IMPORTANT KEYWORD IN OBJECT ORIENTED PROGRAMMING!
# USED TO CREATE NEW USER DEFINED OBJECTS.
# EX2:
# class Square:
#     def __init__(self, x):
#         self.a = x
#
#     def area(self):
#         print self.a * self.a
#
#
# sq = Square(12)
# sq.area()
#
# creates new Square class. Then instantiate the class
# and create an object. (__init__ method, with self and x params)
# then computes the area of the square object


# continue - Don't process more of the loop, do it again.