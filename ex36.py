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


def work_from_home():
    print "Do you live in NYC?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        in_tech_nyc()
    elif choice == "N" or choice == "n":
        in_SF()
    else:
        print "What are you trying to say?"


def in_SF():
    print "Do you live in SF?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Good for you"
        print "Are you in tech?"

        choice = raw_input("Y or N?: ")
        if choice == "Y" or choice == "y":
            print "Sure, why not? Go set up shop in Ritual."
            print " All your coworkers are already there anyway."
        elif choice == "N" or choice == "n":
            print "Why are you even living in SF?"
            print "WF... literally anywhere else."
        else:
            print "Huh?"

    elif choice == "N" or choice == "n":
        print "Not gonna fly"

    else:
        print "What are you trying to say?"


def in_tech_nyc():
    print "Do you work in tech?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        is_winter()
    elif choice == "N" or choice == "n":
        "Probably won\'t fly. Go to the office."
    else:
        print "What are you trying to say?"


def is_winter():
    print "Is it winter?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Is it below 20F?"

        choice = raw_input("Y or N?: ")
        if choice == "Y" or choice == "y":
            is_snowing()
        elif choice == "N" or choice == "n":
            print "Unless you're in the midst of a blizzardy apocolypse,"
            print "go into the office."
        else:
            print "Huh?"

    elif choice == "N" or choice == "n":
        is_summer()
    else:
        print "What are you trying to say?"

def is_snowing():
    print "Is it snowing?"

    choice == raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "How long is the walk to the subway?"

        minutes == raw_input("Number of mins: ")
        if minutes <= 15:
            print "Is there a wintry mix advisary?"

            choice = raw_input("Y or N?: ")
            if choice == "Y" or choice == "y":
                print "Screw that! WFH."
            elif choice == "N" or choice == "n":
                print "Throw on your winter shit and GTFTW!"
                print "(Get The F*ck to Work)"
            else:
                print "What are you trying to say?"

        elif minutes >= 15:
            print "Screw it, work from home."
        else:
            print "Huh?"

    elif choice == "N" or choice == "n":
        print "trains() option to go here"
        exit(0)
    else:
        print "Huh?"

def is_engineer():
    print "Are you a full stack engineer?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Do whatever the hell you want, you hot piece of talent, you!"
    elif choice == "N" or choice == "n":
        work_remote()
    else:
        print "What are you trying to say?"


def is_summer():
    print "Is it summer?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Is it a summer friday?"

        choice = raw_input("Y or N?: ")
        if choice == "Y" or choice == "y":
            print "So since your day is basically over now, "
            print "it would really be counter productive to go in."
            print "WFH"
        elif choice == "N" or choice == "n":
            work_remote()
            # eventually include an option for temp/sunny
            # and if both are good advise to call in sick
        else:
            print "Huh?"
    elif choice == "N" or choice == "n":
        work_remote()
    else:
        print "Huh?"


def work_remote():
    print "Can you actually do your job remotely?"

    choice = raw_input("Y or N?: ")
    if choice == "Y" or choice == "y":
        print "Yeah, fine, work from home"
    elif choice == "N" or choice == "n":
        print "Are you sick?"

        choice == raw_input("Y or N?: ")
        if choice == "Y" or choice == "y":
            print "Yeah, stay home."
            print "Don\'t be that guy who gives everyone the plague"
        elif choice == "N" or choice == "n":
            print "Go the fuck to work"
        else:
            print "Come again?"
    else:
        print "Come again?"


work_from_home()
