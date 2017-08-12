import redditGet

# various functions for every command

# main function that works
# cd [subreddit]
def cd_command(subReddit):
    print 'cd command \n'
    print 'displaying top subs'
    redditGet.main_api_logic(subReddit)

def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    print 'ls command'

def cat_command():
    print 'cat command'

# function to print line
def print_line():
    print '--------------------------------------------------------------------------------------------------------\n'


