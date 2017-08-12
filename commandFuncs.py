import redditGet

# various functions for every command
# <<<<<<< HEAD
# currentSubReddit = 'brisbane'
nextNum = 0
itemsArr = []

# =======
global currentSubReddit
global current_subreddit_sort
# >>>>>>> post-pagination
# main function that works
# cd [subreddit]

default_sort = 'hot'
valid_sorts = ['hot', 'new', 'rising', 'controversial', 'top']

def cd_command(subReddit):
# <<<<<<< HEAD
    # print 'In ' + subReddit[1] + ' subreddit'
    
    resetState(subReddit)    
    
# =======
    global currentSubReddit
    global current_subreddit_sort

    if len(subReddit) > 2:

        new_sort = subReddit[2]

        # TODO: determine if user entered a sort or a dot command


        # if user entered a sort
        if new_sort in valid_sorts:
            current_subreddit_sort = new_sort
        else:
            current_subreddit_sort = default_sort

    else:
        current_subreddit_sort = default_sort

    # Tell the user where they are
    # print 'In ' + currentSubReddit + ' viewing ' + current_subreddit_sort + ' subs'
 
# >>>>>>> post-pagination
def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    global currentSubReddit
    print 'ls command'
# <<<<<<< HEAD
    print 'submissions'
    print currentSubReddit
    redditGet.main_api_logic(currentSubReddit, current_subreddit_sort, 0)

def cat_command():
    print 'cat command'

# function to print line
def print_line():
    print '--------------------------------------------------------------------------------------------------------\n'

def next_command():
    global nextNum
    nextNum += 10
    redditGet.main_api_logic(currentSubReddit, current_subreddit_sort, nextNum)

def resetState(subReddit):
    global currentSubReddit
    global nextNum
    global itemsArr
    currentSubReddit = subReddit
    nextNum = 0
    itemsArr = []

def command_builder():
    print 'in command builder'
