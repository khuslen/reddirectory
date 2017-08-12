# import socket to display username
import socket
import json
import urllib2
import httplib
import time
import praw

# Custom files
import commandFuncs
import redditGet

# bool to keep the program running
programRunning = True

##################################################

#####   NEED TO REFRACTOR FUNCTION IN FILES ######

##################################################
# list of valid commands
valid_commands = ['ls', 'cd', 'cd .', 'cd ..', 'cat', 'exit']

# Function to parse user inputs
def input_parser(user_input):
    global programRunning
    # split user_input to separate command and argument
    user_input_split = user_input.split(' ')

    if user_input_split[0] in valid_commands:
        print 'user entered valid command \n'
        print 'user just entered this:  ' + user_input
        user_input_split = user_input.split(' ')


        if (user_input_split[0] == 'cd'):
            if (user_input_split[1] == '.'):
                commandFuncs.cd_dot_command()
            elif (user_input_split[1] == '..'):
                commandFuncs.cd_dot_dot_command()
            elif (user_input_split[1].isdigit()):
                redditGet.readPost(user_input_split[1]) # read that post number
            else:
                commandFuncs.cd_command(user_input_split[1])

        elif (user_input == 'ls'):
            commandFuncs.ls_command()

        elif (user_input == 'cat'):
            commandFuncs.cat_command()
        
        elif (user_input == 'exit'):
            programRunning = False

    else:
        print 'user entered invalid command'

##################################################
# Constant loop to keep the program running
while (programRunning == True):
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')
    input_parser(user_input)
