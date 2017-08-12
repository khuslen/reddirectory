import main
# list of valid commands
valid_commands = ['ls', 'cd', 'cd .', 'cd ..', 'cat']

# Function to parse user inputs
def input_parser(user_input):
    # split user_input to separate command and argument
    user_input_split = user_input.split(' ')

    if user_input_split[0] in valid_commands:
        print 'user entered valid command \n'
        print 'user just entered this:  ' + user_input
        user_input_split = user_input.split(' ')


        if (user_input_split[0] == 'cd'):
            if (user_input_split[1] == '.'):
                main.cd_dot_command()
            elif (user_input_split[1] == '..'):
                main.cd_dot_dot_command()
            elif (user_input_split[1].isdigit()):
                redditGet.readPost(user_input_split[1]) # read that post number
            else:
                main.cd_command(user_input_split[1])

        elif (user_input == 'ls'):
            main.ls_command()

        elif (user_input == 'cat'):
            main.cat_command()

    else:
        print 'user entered invalid command'

