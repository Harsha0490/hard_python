# use lists, functions, and modules (refer to ex13 if need be)
# draw a map for the game
# code up map

# Should I WFH Today?

# Are you in tech?
# If 'No' end the game here and say
# "Probably won't fly, unless you're dying. better go in"

# Manager/Strict Mode?

# Do you live in NYC? If yes add these questions:
# Has there been an "Earlier Incident" on the train?
# if NYC and Winter: How much walking in commute? Below 30 degrees?

# What Month is it?
# if winter time, ask about sniffles, snow fall, temp.
#
# if summer time, ask about summer friday, meetings, etc.

yes_or_no = choice = raw_input("Y or N?: ")

def work_from_home():
    print "Do you live in NYC?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        in_tech()
    elif choice == "N" or choice == "n":
        in_SF()
    else:
        print "What are you trying to say?"

def in_SF():
    print "Do you live in SF?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":

    elif choice == "N" or choice == "n":
        print "Are you in tech?"

        choice = raw_input("Y or N?: ")
        if choice == "Y" or choice == "y":
            print "Sure, why not? Go set up shop in Ritual for a bit."
            print " All your coworkers are already there anyway."
        elif choice == "N" or choice == "n":
            print "Why are you even living in SF?"
            print "WF... literally anywhere else."
        else:
            print "Huh?"

    else:
        print "What are you trying to say?"

def in_tech():
    print "Do you work in tech?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        is_engineer()
    elif choice == "N" or choice == "n":
        "Probably won\'t fly. Go to the office."
    else:
        print "What are you trying to say?"

def is_engineer():
    print "Are you an engineer?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Do whatever the hell you want, you hot piece of talent, you!"
    elif choice == "N" or choice == "n":
        work_remote()

    else:
        print "What are you trying to say?"

def work_remote():
    print "Can you actually do your job remotely?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Yeah, fine, work from home"
    elif choice == "N" or choice == "n":
        "Unless you\'re dying, go to the office"
    else:
        print "Come again?"
