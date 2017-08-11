# import socket to display username
import socket


# bool to keep the program running
programRunning = True

# list of valid commands
valid_commands = ['ls', 'cd', 'cd .', 'cd ..', 'cat']


##################################################

#####   NEED TO REFRACTOR FUNCTION IN FILES ######

##################################################

# Function to parse user inputs
def input_parser(user_input):
    if user_input in valid_commands:
        print 'user entered valid command \n'
        print 'user just entered this:  ' + user_input

        if (user_input == 'cd'):
            cd_command()

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
def cd_command():
    print 'cd command'

def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    print 'ls command'


def cat_command():
    print 'cat command'


# Constant loop to keep the program running
while (programRunning == True):
    user_input = raw_input(socket.gethostname() + '@' + socket.gethostname() + ':~$ ')
    input_parser(user_input)
