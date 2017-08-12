import redditGet

# various functions for every command
global currentSubReddit
# main function that works
# cd [subreddit]
def cd_command(subReddit):
    global currentSubReddit

    print 'In ' + subReddit + 'subreddit'
    print 'Displaying top subs'
    
    currentSubReddit = subReddit
 
def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    print 'ls command'
    redditGet.main_api_logic(currentSubReddit)

def cat_command():
    print 'cat command'

# function to print line
def print_line():
    print '--------------------------------------------------------------------------------------------------------\n'


