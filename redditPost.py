# Reddit post endoint for creating posts and subs
import praw

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz',
                     username='inter_webz',
                     password='password')


def createSubReddit(currentSubreddit, title):
    print 'creating a sub'
    print currentSubreddit[1]
    print title
    title = title
    # title = 'Test submission from app'
    url = 'https://stackoverflow.com/'
    reddit.subreddit(currentSubreddit[1]).submit(title, url=url)