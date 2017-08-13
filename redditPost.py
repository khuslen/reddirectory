# Reddit post endoint for creating posts and subs
import praw

# create an instance of reddit and subreddit using praw

#### EDIT DETAILS ################################################
reddit = praw.Reddit(client_id='your_id',
                     client_secret='your_key',
                     user_agent='your_username',
                     username='your_username',
                     password=your_password')
##################################################################

def createSubReddit(currentSubreddit, title, body):
    print 'Create a submission in ' + currentSubreddit
    print 'Title' + title
    print 'Body'  + body
    print 'Creating a submission ....'

    # title = 'Test submission from app'
    reddit.subreddit(currentSubreddit).submit(title, selftext= body)
    print 'Submission successful!'
