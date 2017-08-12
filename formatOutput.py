# Change colours
# Print data
import commandFuncs

def printList(items, nextNum, colours):
    CSI="\x1B["
    reset=CSI+"m"
	#print CSI+"31;40m" + "Colored Text" + CSI + "0m"
    end = min(len(items), nextNum+10)
    for i in range(nextNum, end):
        print CSI + colours[i%2] + str(i+1) + '. ' + items[i] + CSI + "0m"

def printPost(submission):
    CSI="\x1B["
    reset=CSI+"m"
    print CSI + "33;40m" + submission.selftext + CSI + "0m"