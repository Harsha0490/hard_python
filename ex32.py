the_count =[1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i


# 1. done
# 2. yes: elements = range(0,6)
# 3. other operations to be used on lists (list functions):
# len(list) - gets length of list
# cmp(list1, list2) - compares elements of two lists
# max(list) - returns item from the list with max value
# min(list) - returns item from the list with min value
# list(seq) - convert a tuple (sequence of immutable Python objects **) into list
#
# other operations to be used on lists (list methods):
# list.append(obj) - appends object obj to list
# list.count(obj) - returns count of how many times obj occurs in list
# list.extend(seq) - appends the contents of seq to list
# list.index(obj) - returns the lowest index in list that obj appears
# list.insert(index, obj) - inserts object obj into list at offset index
# list.pop(obj=list[-1]) - Removes and returns last object or obj from list
# list.remove(obj) - removes object obj from list
# list.reverse() - reverses objects of list in place
# list.sort([func]) - sorts objects of list, use compare function if given

# ** sequences like lists, but tuples cannot be changed and they use parentheses,