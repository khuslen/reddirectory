import commandFuncs

# list of valid commands
# valid_commands = ['ls', 'cd', 'cd .', 'cd ..', 'cat', 'next', 'mkdir', 'help']
valid_commands = ['ls', 'cd', 'cat', 'next', 'mkdir', 'help']

# Function to parse user inputs
def input_parser(user_input):
    # split user_input to separate command and argument
    user_input_split = user_input.split(' ')

    top_level_command = user_input_split[0]

    if top_level_command in valid_commands:
        if (top_level_command == 'cd'):
            commandFuncs.cd_command(user_input_split)

        elif (top_level_command == 'ls'):
            commandFuncs.ls_command()

        elif (top_level_command == 'cat'):
            commandFuncs.cat_command()

        elif (top_level_command == 'next'):
            commandFuncs.next_command()

        elif (top_level_command == 'help'):
            commandFuncs.help_command()

        elif (top_level_command == 'mkdir'):
            info = user_input.split('-t')
            titleAndBody= info[1].split('-u')
            title = titleAndBody[0].replace("'", '')
            body = titleAndBody[1].replace("'", '')
            commandFuncs.mkdir_command(title, body)
    else:
        print 'Please enter a invalid command (enter \"help\" for assistance)'
