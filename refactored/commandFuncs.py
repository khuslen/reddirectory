import redditGet
import userSession

# various functions for every command

default_sort = 'hot'
valid_sorts = ['hot', 'new', 'rising', 'controversial', 'top']

def cd_command(user_input_split):
    if user_input_split[1] == '..':

    elif user_input_split[1] != '.':

    elif user_input_split[1].isdigit():
        redditGet.readPost(int(user_input_split[1]))
        currentSubmission = int(user_input_split[1])

    else:
        print 'In ' + user_input_split[1] + ' subreddit'    

        # Create session object
        currentSession = userSession(user_input_split[1])

        if len(user_input_split) > 2:

            new_sort = user_input_split[2]

            # if user entered a sort
            if new_sort in valid_sorts:
                current_subreddit_sort = new_sort
            else:
                current_subreddit_sort = default_sort
        
    elif (user_input_split[1] == 'comments'):
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

def resetState(subReddit):
    global currentSubReddit
    global nextNum
    global itemsArr
    currentSubReddit = subReddit
    nextNum = 0
    itemsArr = []

def get_state_string():
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
