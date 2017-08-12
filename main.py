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
import userInput

# bool to keep the program running
programRunning = True
##################################################

while (programRunning == True):
    current_prompt = commandFuncs.get_state_string()
    user_input = raw_input(socket.gethostname() + '@' + current_prompt + ':~$ ')

    if user_input != 'exit':
        userInput.input_parser(user_input)
    else:
        programRunning = False
