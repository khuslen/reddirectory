# import socket to display username
import socket
import json
import urllib2
import httplib
import time
import praw


# bool to keep the program running
programRunning = True

# list of valid commands
valid_commands = ['ls', 'cd', 'cd .', 'cd ..', 'cat']


##################################################

#####   NEED TO REFRACTOR FUNCTION IN FILES ######

##################################################

# Function to parse user inputs
def input_parser(user_input):
    # split user_input to separate command and argument
    user_input_split = user_input.split(' ')

    if user_input_split[0] in valid_commands:
        print 'user entered valid command \n'
        print 'user just entered this:  ' + user_input
        user_input_split = user_input.split(' ')


        if (user_input_split[0] == 'cd'):
            cd_command(user_input_split[1])

        elif (user_input == 'cd .'):
            cd_dot_command()

        elif (user_input == 'cd ..'):
            cd_dot_dot_command()

        elif (user_input == 'ls'):
            ls_command()

        elif (user_input == 'cat'):
            cat_command()

    else:
        print 'user entered invalid command'

# various functions for every command

# main function that works
# cd [subreddit]
def cd_command(subReddit):
    print 'cd command \n'
    print 'displaying top subs'
    main_api_logic(subReddit)

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


##################################################

#####   LOGIC FOR API   ##########################

##################################################

# returns top subs with title and score

def main_api_logic(subReddit):
    # create an instance of reddit and subreddit using praw
    # Zak's credentials lolz
    reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                         client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                         user_agent='inter_webz')
    subreddit = reddit.subreddit(subReddit)

    for submission in subreddit.top(limit=10):
        print_line()
        print ('Title: ')
        print(submission.title)  # Submission title
        print ('Score: ')
        print (submission.score)  # Submission Score


# Constant loop to keep the program running
while (programRunning == True):
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')
    input_parser(user_input)
