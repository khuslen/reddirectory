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
# Constant loop to keep the program running
while (programRunning == True):
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')
    userInput.input_parser(user_input)
