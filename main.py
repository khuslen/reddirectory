# import socket to display username
import socket

programRunning = True


# Function to parse user inputs
def input_parser(user_input):
    print 'user just entered this:  ' + user_input


# Constant loop to keep the program running
while (programRunning == True):
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')
    input_parser(user_input)
