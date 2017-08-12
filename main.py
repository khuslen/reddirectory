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

def getUserInput():
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')
    return user_input

while (programRunning == True):
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')

    if user_input != 'exit':
        userInput.input_parser(user_input)
    else:
        programRunning = False
