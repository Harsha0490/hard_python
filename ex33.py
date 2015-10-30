def whileLoopEx(upperLimit, step):
    i = 0
    numbers = []

    while i < upperLimit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


numbers = whileLoopEx(6, 2)

print "The numbers: "

for num in numbers:
    print num


i = 0
numbers = []

for i in range(0, 10):
    print "Adding %d to numbers." % i
    numbers.append(i)

print numbers

# Original Code:
# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
# print "The numbers: "
#
# for num in numbers:
#     print num