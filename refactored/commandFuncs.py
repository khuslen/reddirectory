import userSession
import redditGet
import redditPost
import helpInfo

default_sort = 'hot'
valid_sorts = ['hot', 'new', 'rising', 'controversial', 'top']

def cd_command(user_input_split):

    if user_input_split[1] == '.':
        cd_dot_command()

    elif user_input_split[1] == '..':
        cd_dot_dot_command()

    elif user_input_split[1][:3] == '../':
        get_dots = user_input_split[1].split('/')
        for x in range(0, len(get_dots)):
            cd_dot_dot_command()

    elif user_input_split[1].isdigit():
        if userSession.currentSession.currentState == 'subreddit':
            userSession.currentSession.currentThread = int(user_input_split[1])
            userSession.currentSession.currentState = 'thread'
        
        elif userSession.currentSession.currentState == 'thread':
            userSession.currentSession.currentSubmission = int(user_input_split[1])
            userSession.currentSession.currentState = 'submission'
            redditGet.readPost(int(user_input_split[1]))

        elif userSession.currentSession.currentState == 'submission':
            userSession.currentSession.currentComment = int(user_input_split[1])
            userSession.currentSession.currentState = 'comment'
        
        elif userSession.currentSession.currentState == 'comment':
            # TODO:
            print "hi"

    elif userSession.currentSession.currentState == 'attheverystartoftheprogram':
        userSession.currentSession.resetSession()
        userSession.currentSession.currentSubreddit = user_input_split[1]
        userSession.currentSession.currentState = 'thread'
    
    elif userSession.currentSession.currentState == 'subreddit':
        userSession.currentSession.currentState = 'thread'
        userSession.currentSession.currentThread = 'hot'
        if user_input_split[1] in valid_sorts:
            userSession.currentSession.currentThread = user_input_split[1]
        userSession.currentSession.resetThread()

def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    # print 'cd .. command'
    if userSession.currentSession.currentState == 'subreddit':
        userSession.currentSession.currentSubreddit = ""
        userSession.currentSession.currentState = 'attheverystartoftheprogram'
    elif userSession.currentSession.currentState == 'thread':
        userSession.currentSession.currentThread = ""
        userSession.currentSession.currentState = 'subreddit'
    elif userSession.currentSession.currentState == 'submission':
        userSession.currentSession.currentSubmission = ""
        userSession.currentSession.currentState = 'thread'
    elif userSession.currentSession.currentState == 'comment':
        userSession.currentSession.currentComment = ""
        userSession.currentSession.currentState = 'submission'

def ls_command():
    if userSession.currentSession.currentState == 'thread':
        redditGet.main_api_logic(userSession.currentSession.currentSubreddit, userSession.currentSession.currentThread, userSession.currentSession.nextNum)
    elif userSession.currentSession.currentState == 'subreddit':
        printThreads()
    elif userSession.currentSession.currentState == 'submission':
        redditGet.readComments(userSession.currentSession.currentSubmission)
    elif userSession.currentSession.currentState == 'comment':
        # TODO: Display subcomments
        print "hi 2"

def printThreads():
    print "Please enter one of the following "
    print valid_sorts

def cat_command():
    # TODO: cat
    print 'cat command'

def next_command():
    userSession.currentSession.nextNum += 10
    redditGet.main_api_logic(userSession.currentSession.currentSubreddit, userSession.currentSession.currentThread, userSession.currentSession.nextNum)

def mkdir_command(title, body):
    redditPost.createSubReddit(userSession.currentSession.currentSubreddit, title, body)

def help_command():
    helpInfo.printHelpInfo()
