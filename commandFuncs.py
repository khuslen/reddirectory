import redditGet

# various functions for every command
currentSubReddit = 'brisbane'
nextNum = 0
itemsArr = []
currentSubmission = 'something'

# main function that works
# cd [subreddit]

def cd_command(subReddit):
    print 'In ' + subReddit + ' subreddit'
    
    resetState(subReddit)    
    
def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    global currentSubReddit
    print 'ls command'
    print 'submissions'
    redditGet.main_api_logic(currentSubReddit, 0)

def cat_command():
    print 'cat command'

# function to print line
def print_line():
    print '--------------------------------------------------------------------------------------------------------\n'

def next_command():
    global nextNum
    nextNum += 10
    redditGet.main_api_logic(currentSubReddit, nextNum)

def resetState(subReddit):
    global currentSubReddit
    global nextNum
    global itemsArr
    currentSubReddit = subReddit
    nextNum = 0
    itemsArr = []
   
