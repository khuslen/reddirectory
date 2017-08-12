import json
#import urllib2
#import httplib
#import time
import praw
from praw.models import MoreComments

# Custom files
import commandFuncs


##################################################

#####   LOGIC FOR API   ##########################

##################################################

# returns top subs with title and score

itemsArr = []
subId = []

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz')

def main_api_logic(subReddit):
    # Stores the listed items in an array so we can access them with a number
    global itemsArr


    subreddit = reddit.subreddit(subReddit)
    
    itemNum = 1
    for submission in subreddit.hot(limit=10):
        commandFuncs.print_line()
        
        itemsArr.append(submission)

        print (str(itemNum) + '. Title: ')
        print(submission.title)  # Submission title
        print ('Score: ')
        print (submission.score)  # Submission Score
        subId.append(submission.id)
        itemNum += 1

def readPost(itemNum):
    counter = 1
    print 'reading post'
    submission = reddit.submission(subId[itemNum -1])
    print (submission.selftext)

    # for top_level_comment in submission.comments:
    #     if isinstance(top_level_comment, MoreComments):
    #         continue
    #     print(str(counter) + '. '+ top_level_comment.body)
    #     counter += 1
    # Add code here that displays the main post and its comments

    # TO-DO: Display the contents of itemsArr[itemNum]

def readComments(itemNum):
    counter = 1
    print 'read comments'
    submission = reddit.submission(subId[itemNum - 1])
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print(str(counter) + '. ' + top_level_comment.body)
        counter += 1
        # Add code here that displays the main post and its comments

        # TO-DO: Display the contents of itemsArr[itemNum]