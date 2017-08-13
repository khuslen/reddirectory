# Change colours
# Print data
import commandFuncs

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def printList(names, items, nextNum, colours):
    CSI="\x1B["
    reset=CSI+"m"
    #print CSI+"31;40m" + "Colored Text" + CSI + "0m"
    end = min(len(items), nextNum+10)
    for i in range(nextNum, end):
        print color.YELLOW + str(i+1) + '. ' + color.BOLD + names[i] + ": " + color.END + CSI + colours[i%2] + items[i] + CSI + "0m"

def printPost(submission):
    CSI="\x1B["
    reset=CSI+"m"
    print CSI + "33;40m" + submission.selftext + CSI + "0m"

def displayTitle(prefix, title):
    CSI="\x1B["
    reset=CSI+"m"
    return CSI + "35;40m" + prefix + title + CSI + "0m"

# def printList(names, items, nextNum, colours):
#     CSI="\x1B["
#     reset=CSI+"m"
# 	#print CSI+"31;40m" + "Colored Text" + CSI + "0m"
#     end = min(len(items), nextNum+10)
#     for i in range(nextNum, end):
#         print CSI + colours[i%2] + str(i+1) + '. ' + names[i] + ": " + items[i] + CSI + "0m"

# def printPost(submission):
#     CSI="\x1B["
#     reset=CSI+"m"
#     print CSI + "33;40m" + submission.selftext + CSI + "0m"

# def displayTitle(prefix, title):
#     CSI="\x1B["
#     reset=CSI+"m"
#     return CSI + "35;40m" + prefix + title + CSI + "0m"