def printHelpInfo():
    print 'Valid commands: \n'
    print '\tls, cd, cd .., next, prev, mkdir, help\n'
    print 'Navigating through the subs \n'
    print '\t~$ cd [subreddit] \n'

    print 'Navigating into a submission \n'
    print '\t~$ cd [postNumber] (int)\n'

    print 'To view the submissions in a subreddit, or \n'
    print 'to view the comments in a submission\n'
    print '\t~$ ls\n'

    print 'Post submission on a subreddit\n'
    print 'Navigate to the appropriate subreddit then\n'
    print '\t~$ mkdir -t [title] -u [body of the post]\n'

    print 'To view the next set of submissions or comments \n'
    print '\t~$ next \n'
    print 'To view the previous set of submissions or comments \n'
    print '\t~$ prev \n'
