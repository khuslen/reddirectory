import redditGet
import redditPost
import helpInfo

# various functions for every command
# currentSubReddit = 'brisbane'
nextNum = 0
itemsArr = []
# currentSubmission = 'something'

global currentSubReddit
global current_subreddit_sort
# main function that works
# cd [subreddit]

default_sort = 'hot'
valid_sorts = ['hot', 'new', 'rising', 'controversial', 'top']

def cd_command(subReddit):
    # print 'In ' + subReddit[1] + ' subreddit'
    
    resetState(subReddit)    
    global currentSubReddit
    global current_subreddit_sort
    global currentSubmission

    if len(subReddit) > 2:

        new_sort = subReddit[2]

        # TODO: determine if user entered a sort or a dot command


        # if user entered a sort
        if new_sort in valid_sorts:
            current_subreddit_sort = new_sort
        else:
            current_subreddit_sort = default_sort

    elif (subReddit[1].isdigit()):
        redditGet.readPost(int(subReddit[1]))
        currentSubmission = int(subReddit[1])
    elif (subReddit[1] == 'comments'):
        redditGet.readComments(currentSubmission)


    else:
        current_subreddit_sort = default_sort

    # Tell the user where they are
    # print 'In ' + currentSubReddit + ' viewing ' + current_subreddit_sort + ' subs'
 
def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    global currentSubReddit
    print 'ls command'
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

def mkdir_command(title, body):
    redditPost.createSubReddit(currentSubReddit, title, body)

def help_command():
    helpInfo.printHelpInfo()

def resetState(subReddit):
    global currentSubReddit
    global nextNum
    global itemsArr
    currentSubReddit = subReddit
    nextNum = 0
    itemsArr = []

def get_state_string():

    global currentSubReddit
    global nextNum
    global itemsArr
    global currentSubmission

    new_prompt_arr = []

    if 'currentSubReddit' in globals():
        new_prompt_arr.append(currentSubReddit[1])

        if 'current_subreddit_sort' in globals():
            new_prompt_arr.append(current_subreddit_sort)

            if 'currentSubmission' in globals():
                new_prompt_arr.append(str(currentSubmission))

    else: 
        new_prompt_arr.append('reddit')

    new_prompt_str = '/'.join(new_prompt_arr)

    return new_prompt_str
