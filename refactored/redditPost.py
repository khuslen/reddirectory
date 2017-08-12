# Reddit post endoint for creating posts and subs
import praw

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz',
                     username='inter_webz',
                     password='password')


def createSubReddit(currentSubreddit, title, body):
    print 'create a sumission in ' + currentSubreddit
    print 'Title' + title
    print 'Body'  + body
    print 'creating a submission ....'

    # title = 'Test submission from app'
    reddit.subreddit(currentSubreddit).submit(title, selftext= body)
    print 'submission successfull'